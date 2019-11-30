import random
import unittest
import json
import fib_app
from flask import Flask, request, jsonify
from fib_app.custom_exceptions import CacheMissException, FibonacciException, TooLargeValueException, ValueTooSmallException, StartCannotBeGreaterThanEndException
from fib_app.indx_calculator import FibbonacciIndexingLogic
from fib_app.fibonacci import Fibonacci
from fib_app.cache import FibonacciNumberCache
from fib_app.interfaces import FibonacciCacheInterface
from fib_app.orchestrator import FibonacciIndexed


class FlaskTestCase(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def setUp(self):
        FibonacciNumberCache().clean()
        app=fib_app.create_app()
        app.debug = True
        self.app = app.test_client()
    
    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/health') 
        data = json.loads(result.get_data(as_text=True))
        self.assertEqual(data.get('hit_percentage'), 0) 
        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 
    

    def test_indexed_3_5(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/fib/3/5') 

        # assert the response data
        self.assertEqual(int(result.data) , 10)
    
    def test_indexed_5_3(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/fib/5/3') 
        self.assertEqual(result.status_code , 400)
    
    def test_check_health(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.app.get('/fib/4/5') 
        self.app.get('/fib/1/5') 
        self.app.get('/fib/3/5') 
        result = self.app.get('/health') 
        data = json.loads(result.get_data(as_text=True))
        # assert the response data
        self.assertEqual(data.get('hit_percentage') , 50)
    
    def test_indexed_start_too_small(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/fib/-1/5') 
        self.assertEqual(result.status_code , 400)
    
    def test_indexed_end_too_small(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/fib/1/-5') 
        self.assertEqual(result.status_code , 400)

       