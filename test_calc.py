import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):
    # def setUp(self):
    #     print('Creating calc')
    #     # self.calc = Calculator()  
        
    def test_plus(self):
        cases = [
            {
                'first': 100,
                'second': 200,
                'expected': 300,  
            },
            {
                'first': 0,
                'second': 0,
                'expected': 0,  
            },
            {
                'first': -100,
                'second': 200,
                'expected': 100,  
            },
            {
                'first': -5,
                'second': -9,
                'expected': -14,  
            },
        ]

        for case in cases:
            first = case['first']
            second = case['second']
            self.assertEqual(case['expected'], Calculator.plus(first, second))
    
    def test_minus(self):
        cases = [
            {
                'first': 300,
                'second': 200,
                'expected': 100,  
            },
            {
                'first': 0,
                'second': 0,
                'expected': 0,  
            },
            {
                'first': -100,
                'second': 200,
                'expected': -300,  
            },
            {
                'first': -5,
                'second': -9,
                'expected': 4,  
            },
        ]
        for case in cases:
            first = case['first']
            second = case['second']
            self.assertEqual(case['expected'], Calculator.minus(first, second))
            
    
    def test_multiply(self):
        cases = [
            {
                'first': 5,
                'second': 5,
                'expected': 25,  
            },
            {
                'first': 0,
                'second': 0,
                'expected': 0,  
            },
            {
                'first': 200,
                'second': 4,
                'expected': 800,  
            },
            {
                'first': -5,
                'second': 9,
                'expected': -45,  
            },
            {
                'first': 5,
                'second': -9,
                'expected': -45,  
            },
            {
                'first': 0,
                'second': 100000,
                'expected': 0,  
            },   
        ]
        for case in cases:
            first = case['first']
            second = case['second']
            self.assertEqual(case['expected'], Calculator.multiply(first, second))
            
    def test_divide(self):
        cases = [
            {
                'first': 100,
                'second': 200,
                'expected': 0.5,  
            },
            {
                'first': 0,
                'second': 200,
                'expected': 0,  
            },
            {
                'first': 81,
                'second': 9,
                'expected': 9,  
            },
            {
                'first': 81,
                'second': -9,
                'expected': -9,  
            },
            {
                'first': -81,
                'second': 9,
                'expected': -9,  
            },
        ]

        for case in cases:
            first = case['first']
            second = case['second']
            self.assertEqual(case['expected'], Calculator.divide(first, second))
            
        self.assertRaises(ZeroDivisionError, Calculator.divide, 25, 0)
            
    def tearDown(self):
        print('Tear down...')