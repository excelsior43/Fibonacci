import time
from fib_app.custom_exceptions import TooLargeValueException, CacheMissException, ValueTooSmallException, StartCannotBeGreaterThanEndException
import fib_app
from fib_app.indx_calculator import FibbonacciIndexingLogic
"""
This is a composit class that does calculations using 2 classes
1) Fibonacci class
2) FibonacciNumberCache class
3) FibbonacciIndexingLogic class
"""
class FibonacciIndexed:
    def __init__(self, fib, cache):
        self.fib=fib
        self.cache=cache
        
    
    '''
    This function finds the Fibonacci sum between two indexes
    I defined Benchmarking : totalTimeTaken/magnitued
    here totalTimeTaken is the timetaken for this operation
    NOTE:  magnitued = endIndex , I took endIndex as 'magnitude' because 
    to generate a fibonacci series we have to iterate from start to end number.
    '''
    def fibonacci_indexed(self, startIndex, endIndex):
        fib_app.checkRange(startIndex, endIndex)
        startTime = time.time()
        
        theCachedIndexes=self.cache.getCachedList(startIndex,endIndex)
        indxLogic=FibbonacciIndexingLogic(startIndex, endIndex, theCachedIndexes)

        sum =0
        for i in indxLogic.getGenerateNextValue(): 
            if(isinstance(i, int)):
                sum = sum+self.get_fib(i)
                print("calculating fib of "+str(i))
            else:
                sum = sum+int(i[2])
                print("getting cached value ")
        totalTime = time.time()-startTime
        self.cache.storeCachedList(startIndex, endIndex, sum)
        return sum

    def get_fib(self, n):
        try:
            retValue=self.cache.get(n)
        except(CacheMissException):
            retValue=self.cache.put(n, self.fib.fibonacci(n))
        return int(retValue)