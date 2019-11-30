import unittest 
from fib_app.cache import FibonacciNumberCache
from fib_app.custom_exceptions import CacheMissException

class FibonacciCacheTestClass(unittest.TestCase): 
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
        
        self.cache=FibonacciNumberCache()
        self.cache.clean()
        pass 

    # clean up logic
    # code that is executed after each test
    def tearDown(self):
        self.cache.clean()
        pass 

    def test_clear_cache(self):
        self.cache.put(3, 10)
        self.cache.clean()
        with self.assertRaises(CacheMissException) as context:
            self.cache.get(3)
            
    def test_cache_for_exception(self):
        with self.assertRaises(CacheMissException) as context:
            self.cache.get(2843)
    
    def test_cache_put_get(self):
        self.cache.put(3, 10)
        self.assertEqual(10, int(self.cache.get(3))) 
    
    def test_cache_health(self):
        self.cache.put(23, 100)
        self.assertEqual(100, int(self.cache.get(23))) 
        try:
            self.cache.get('non_existent_key')
        except(CacheMissException):
            pass
        self.assertEqual(50, self.cache.get_health().get('hit_percentage'))

    def test_cache_health_none(self):
        self.assertEqual(0, self.cache.get_health().get('hit_percentage'))

