import unittest 
from fib_app.custom_exceptions import CacheMissException, FibonacciException, TooLargeValueException, ValueTooSmallException, StartCannotBeGreaterThanEndException
from fib_app.indx_calculator import FibbonacciIndexingLogic
from fib_app.fibonacci import Fibonacci
from fib_app.cache import FibonacciNumberCache
from fib_app.interfaces import FibonacciCacheInterface
from fib_app.orchestrator import FibonacciIndexed

class FibonacciIndexLogicTestClass(unittest.TestCase): 

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
    pass 

  # clean up logic
  # code that is executed after each test
  def tearDown(self):
    pass 

  # test method for index 10
  def test_fib_with_index_3_5(self):
    theList=["1:1:1", "3:5:10","7:8:42","8:11:55"]
    fibIndexedCache=FibbonacciIndexingLogic(3,9,theList)
    theFinalList=[]
    for i in fibIndexedCache.getGenerateNextValue():
        theFinalList.append(str(i))
    self.assertEqual(theFinalList, ['3', '4', '5', '6', '7', '8', '9'])
