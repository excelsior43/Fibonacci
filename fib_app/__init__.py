from flask import render_template

from fib_app.custom_exceptions import CacheMissException, FibonacciException, TooLargeValueException, ValueTooSmallException, StartCannotBeGreaterThanEndException
from fib_app.indx_calculator import FibbonacciIndexingLogic
from fib_app.fibonacci import Fibonacci
from fib_app.cache import FibonacciNumberCache
from fib_app.interfaces import FibonacciCacheInterface
from fib_app.orchestrator import FibonacciIndexed

from flask import Flask, request, jsonify
import os
from flask import Flask, jsonify

MAX_ALLOWED_VALUE=1000
FIB_INDEX_SET='fibIndexedSet'
CACHE_MISSES='fibonacci:CACHE_MISS_COUNTER'
CACHE_HITS='fibonacci:CACHE_HIT_COUNTER'
ZFILL=210

'''
Zfill is used for caching the number in redis 
it is number of digits for fib(MAX_ALLOWED_VALUE), in this case fib(10000) has 210 digits in the value
this would be used like this : str(165).zfill(4)

Just for Information :  
 for 1000  ->  210 digits
 for 10000 -> 2091 digits
'''

'''
fib_app is used to find the fibonacci
'''
def create_app(config=None):
    
    print ("inside create_app")
    app = Flask(__name__)
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})
    cache=FibonacciNumberCache()
    cache.clean()

    @app.route('/fib/<string:startIndex>/<string:endIndex>')
    def getFibByIndex(startIndex, endIndex):
        start=int(startIndex)
        if(start <=0 ):
            raise ValueTooSmallException("StartIndex is too small : "+startIndex)
        end=int(endIndex)
        if(end<=0):
            raise ValueTooSmallException("EndIndex is too small : "+endIndex)

        if(start >MAX_ALLOWED_VALUE ):
            raise TooLargeValueException("StartIndex ("+startIndex+") is too large, allowed value should be < "+MAX_ALLOWED_VALUE)
        end=int(endIndex)
        if(end>MAX_ALLOWED_VALUE):
            raise TooLargeValueException("EndIndex ("+endIndex+") is too large, allowed value should be < "+MAX_ALLOWED_VALUE)
        if(start >end):
            raise StartCannotBeGreaterThanEndException("StartIndex ("+str(start)+ ") value is greater than EndIndex("+str(end)+")")
        fibIndex=FibonacciIndexed(Fibonacci(), cache)
        return str(fibIndex.fibonacci_indexed(start, end))

    @app.route('/health')
    def test_script():
        return jsonify(cache.get_health())
    
    @app.errorhandler(FibonacciException)
    def all_exception_handler(error):
        return error.code, error.status

    return app

def checkRange(startIndex, endIndex):
    start=int(startIndex)
    end=int(endIndex)
    if start < 0 or end <0:
        message = "Invalid input. " + str(start)+", " +str(end)+ " should not be  positive numbers" 
        raise ValueTooSmallException(message)
    if start >MAX_ALLOWED_VALUE  or end >MAX_ALLOWED_VALUE:
        message = "Invalid input. " + str(startIndex)+", " +str(end)+ " should not be  > numbers" +str(MAX_ALLOWED_VALUE)
        raise TooLargeValueException(message)
    if end < start:
            message = "Invalid input. " + str(start) + " should be a less than "+ str(end) 
            raise StartCannotBeGreaterThanEndException(message)



