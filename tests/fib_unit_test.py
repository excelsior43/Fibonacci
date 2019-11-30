import unittest 
from fib_app.custom_exceptions import CacheMissException, FibonacciException, TooLargeValueException, ValueTooSmallException, StartCannotBeGreaterThanEndException
from fib_app.indx_calculator import FibbonacciIndexingLogic
from fib_app.fibonacci import Fibonacci
from fib_app.cache import FibonacciNumberCache
from fib_app.interfaces import FibonacciCacheInterface
from fib_app.orchestrator import FibonacciIndexed

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
    
    self.fib=Fibonacci()
    pass 

  # clean up logic
  # code that is executed after each test
  def tearDown(self):
    pass 

  # test method for index negative value
  def test_if_fib_1_is_negative(self):
    with self.assertRaises(ValueTooSmallException) as context:
      self.fib.fibonacci(-101)
  
    # test method for index 1
  def test_if_fib_0_is_0(self):
    self.assertEqual(0, self.fib.fibonacci(0)) 

  # test method for index 1
  def test_if_fib_1_is_1(self):
    self.assertEqual(1, self.fib.fibonacci(1)) 

  # test method for index 2
  def test_if_fib_2_is_1(self):
    self.assertEqual(1, self.fib.fibonacci(2)) 
  
   # test method for index 1
  def test_if_for_fib_5(self):
    self.assertEqual(5, self.fib.fibonacci(5)) 
  
   # test method for index 10
  def test_if_for_fib_10(self):
    self.assertEqual(55, self.fib.fibonacci(10)) 

  
  # test method for index negative value
  def test_if_is_too_large(self):
    with self.assertRaises(TooLargeValueException) as context:
      self.fib.fibonacci(100001)