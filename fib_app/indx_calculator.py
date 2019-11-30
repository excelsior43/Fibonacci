from fib_app.custom_exceptions import FibonacciException, TooLargeValueException, ValueTooSmallException, StartCannotBeGreaterThanEndException
import fib_app
"""
this is the backbone of the whole application.
Here the caching logic to cache between 2 points is decided and the already existing caches are loaded
I have written a generator function to achieve this.

"""
class FibbonacciIndexingLogic:
    def __init__(self, start, end, cachedList):
        
        self.start=start
        self.end=end
        self.cachedList=cachedList
    
    def getParsedTuple(self, tup):
        return tup.split(":")

    def checkTuple(self, value, theTuple):
        if(isinstance(theTuple, tuple)== False):
            return False
        try:
            theValues=theTuple.split(":")
            sVal=int(theValues[0])
            eVal=int(theValues[1])
            #check if the tuple length is exactly 3
            if(len(theValues) !=3):
                return False
            #check if the tuple start and end values are in the window (between start and end index)
            if(sVal<self.start or eVal >self.end):
                return False
            if(value >=sVal and value<=eVal ):
                return True
        except:
            return False

    def isItInList(self, val):
        for i in self.cachedList: 
            if(self.checkTuple(val, i)):
                return i
        return None

    def getGenerateNextValue(self):
        fib_app.checkRange(self.start, self.end)
        r = range(self.start, self.end+1)
        i=self.start
        while(i<=self.end):
            inList=self.isItInList(i)
            if( inList !=None):
                tpl=self.getParsedTuple(inList)
                yield tpl
                # here the index is incremented by the cached instance endIndex
                i=int(tpl[1])+1
            else:
                yield i
                i=i+1




