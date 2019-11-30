from fib_app.custom_exceptions import TooLargeValueException, ValueTooSmallException

from fib_app.cache import FibonacciNumberCache
import fib_app
"""
    class that returns Fibonacci of any given number

    0 1 2 3 4 5 6  7  8  9 
    0 1 1 2 3 5 8 13 21 34 
"""
class Fibonacci:
    def __init__(self):
        pass
    def fibonacci(self, n): 
        if(n<0):
            raise ValueTooSmallException(str(n) +" is too small : ")
        if(n>= fib_app.MAX_ALLOWED_VALUE):
            raise TooLargeValueException(str(n)+" is too large : should be < "+str(fib_app.MAX_ALLOWED_VALUE))
        a = 0
        b = 1
        if n == 0: 
            return a 
        elif n == 1: 
            return b 
        else: 
            for i in range(2,n+1): 
                c = a + b 
                a = b 
                b = c 
            return b 