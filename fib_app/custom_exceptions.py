import sys

'''
This is the generic exception 
'''
class FibonacciException(Exception): 
    """Raised when the input value is too small"""
    def __init__(self, code):
        self.code = code
        self.status=400

'''
This is raised if fib(n) is not found in cache
'''
class CacheMissException(FibonacciException): 
    """Raised when the input value is too small"""
    def __init__(self, code):
        super().__init__(code)
'''
This is raised if starindex or endindex is <0
'''
class ValueTooSmallException(FibonacciException): 
    """Raised when the input value is too small"""
    def __init__(self, code):
        super().__init__(code)

'''
This is raised if starindex > endindex as this is incorrect input.
'''
class StartCannotBeGreaterThanEndException(FibonacciException): 
    """Raised when the input value is too small"""
    def __init__(self, code):
        super().__init__(code)


'''
This is raised if starindex > endindex as this is incorrect input.
'''
class TooLargeValueException(FibonacciException): 
    """Raised when the input value is too small"""
    def __init__(self, code):
        super().__init__(code)