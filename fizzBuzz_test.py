import unittest
from FizzBuzzValueChecker import *

class FizzBuzzTest(unittest.TestCase):

    def test_0_raises_error(self):
        value = 0
        self.assertRaises(Value0Error, FizzBuzzValueChecker.checkValue, value)

    def test_negative_raises_error(self):
        value = -1
        self.assertRaises(NegativeValueError, FizzBuzzValueChecker.checkValue, value)

    def test_multiple_of_3_returns_Fizz(self):
        value = 3
        actual = FizzBuzzValueChecker.checkValue(value)
        self.assertEqual("Fizz", actual)