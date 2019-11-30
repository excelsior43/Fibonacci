import unittest 
from fib_app.custom_exceptions import CacheMissException, FibonacciException, TooLargeValueException, ValueTooSmallException, StartCannotBeGreaterThanEndException
from fib_app.indx_calculator import FibbonacciIndexingLogic
from fib_app.fibonacci import Fibonacci
from fib_app.cache import FibonacciNumberCache
from fib_app.interfaces import FibonacciCacheInterface
from fib_app.orchestrator import FibonacciIndexed

class DummyCache(FibonacciCacheInterface):
   
    def get(self, b):
        raise CacheMissException("Dummy exception, cache missed ")
    def put(self, n, val):
        super().put(n, val)  
        return val
    def getCachedList(self,a,b):
        for i in range(3,5):
          yield str(i)
    def storeCachedList(self, startIndex, endIndex, sum):
        pass
    
     

"""
Fibonacci class is being tested here.
1 2 3 4 5
1 1 2 3 5
"""
class FibonacciTestClass(unittest.TestCase): 

  # initialization logic for the test suite declared in the test module
  # code that is executed before all tests in one test run
  @classmethod
  def setUpClass(cls):
       pass 

  # clean up logic for the test suite declared in the test module
  # code that is executed after all tests in one test run
  @classmethod
  def tearDownClass(cls):
       pass 

  # initialization logic
  # code that is executed before each test
  def setUp(self):
    FibonacciNumberCache().clean()
    self.fibIndex=FibonacciIndexed(Fibonacci(), DummyCache())
    pass 

  # clean up logic
  # code that is executed after each test
  def tearDown(self):
    pass 

  # test method for index 10
  def test_fib_with_index_3_5(self):
    self.assertEqual(10, self.fibIndex.fibonacci_indexed(3,5))

  # test method for startindex morethan endindex
  def test_if_index_start_morethan_end(self):
    with self.assertRaises(StartCannotBeGreaterThanEndException) as context:
      self.fibIndex.fibonacci_indexed(10, 5)

  # test method for startindex morethan endindex
  def test_if_index_startindex_negative(self):
    with self.assertRaises(ValueTooSmallException) as context:
      self.fibIndex.fibonacci_indexed(-1, 5)
  
    # test method for startindex morethan endindex
  def test_if_index_endindex_negative(self):
    with self.assertRaises(ValueTooSmallException) as context:
      self.fibIndex.fibonacci_indexed(1, -15)


  # test method for startindex morethan endindex
  def test_if_index_startindex_too_large(self):
    with self.assertRaises(TooLargeValueException) as context:
      self.fibIndex.fibonacci_indexed(100001, 5)
  
    # test method for startindex morethan endindex
  def test_if_index_endindex_too_large(self):
    with self.assertRaises(TooLargeValueException) as context:
      self.fibIndex.fibonacci_indexed(1, 100000)

