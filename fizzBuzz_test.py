import unittest
from FizzBuzzValueChecker import FizzBuzzValueChecker
from FizzBuzzValueChecker import IncorrectValueError

class FizzBuzzTest(unittest.TestCase):

    def test_0_raises_error(self):
        value = 0
        self.assertRaises(IncorrectValueError, FizzBuzzValueChecker.checkValue, value)

    def test_negative_raises_error(self):
        value = -1
        self.assertRaises(IncorrectValueError, FizzBuzzValueChecker.checkValue, value)

    def test_multiple_of_3_returns_Fizz(self):
        value = 3
        actual = FizzBuzzValueChecker.checkValue(value)
        self.assertEqual("Fizz", actual)

    def test_multiple_of_5_returns_Buzz(self):
        value = 10
        actual = FizzBuzzValueChecker.checkValue(value)
        self.assertEqual("Buzz", actual)

    def test_multiple_of_3_and_5_returns_Buzz(self):
        value = 15
        actual = FizzBuzzValueChecker.checkValue(value)
        self.assertEqual("FizzBuzz", actual)

    def test_matches_no_case_returns_value(self):
        value = 4
        actual = FizzBuzzValueChecker.checkValue(value)
        self.assertEqual(value, actual)