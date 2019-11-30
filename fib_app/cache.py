import redis
from fib_app.custom_exceptions import CacheMissException
from fib_app.interfaces import FibonacciCacheInterface
import fib_app

'''
This is Fibonacci Cache class that is used to 
    1. save the fib(n) if it do not exist, adds to CACHE_MISSES 
    2. return fib(n) if it exist, adds to CACHE_HITS 
'''


class FibonacciNumberCache(FibonacciCacheInterface):
    'Fibonacci Cache maintains cache of all the generated numbers'
    def __init__(self):
        # step 2: define our connection information for Redis
        # Replaces with your configuration information
        redis_host = "localhost"
        redis_port = 6379
        redis_password = ""
        self.cacheMisses=0
        self.cacheHits=0
        # step 3: create the Redis Connection object
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.    
        self.r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        self.clean()

    '''
    cleanup method when the application is freshly loaded
    '''
    def clean(self):
        self.r.flushall()
    '''
        Looks for the fib(n) in cache 
            returns it when found.
            else raised a CacheMissException
    '''
    def get(self, n):
        """This function chacks if the given number exists in cache"""
        theValue=self.r.get("fibonacci:"+str(n))
        if(theValue==None):
            self.r.incr(fib_app.CACHE_MISSES, 1)
            raise CacheMissException("Cache Entry not found for : "+str(n))
        else:
            self.r.incr(fib_app.CACHE_HITS, 1)
        return theValue
    '''
        puts fib(n) in cache 
    '''
    def put(self, n, val):
        self.r.set("fibonacci:"+str(n), val)
        return val
    '''
        retuens the health of application.
        returns : total hits, cache misses and cache hits and cache hit%
        NOTE: My assumtion is that cache hit percentage defines the health of application
    '''
    def get_health(self):
        misses=hits=0
        if (self.r.get(fib_app.CACHE_MISSES) !=None):
            misses=int(self.r.get(fib_app.CACHE_MISSES));
        if (self.r.get(fib_app.CACHE_HITS) !=None):
            hits=int(self.r.get(fib_app.CACHE_HITS));
        count=misses+hits
        if (count !=0):
            percentage=((hits / count )* 100)
        else:
            percentage=0
        return { 'misses' : misses, 'hits' :hits, 'count' : count, 
                 'hit_percentage' : percentage }

    def getCachedList(self, start, end):
        zeroFill=str(0).zfill(fib_app.ZFILL)
        min = '[' + str(start).zfill(fib_app.ZFILL)+":"+zeroFill+":"+zeroFill
        max= '[' + str(end).zfill(fib_app.ZFILL)+":"+zeroFill+":"+zeroFill
        result=self.r.zrangebylex(fib_app.FIB_INDEX_SET, min, max)
        print(result)
        return result
    
    def storeCachedList(self, start, end, value):
        data=str(start).zfill(fib_app.ZFILL)+":"+str(end).zfill(fib_app.ZFILL)+":"+str(value).zfill(fib_app.ZFILL)
        self.r.zadd(fib_app.FIB_INDEX_SET, {data: 0})
        print("Added index "+str(start) +":"+ str(end) +":"+str(value) )
 




