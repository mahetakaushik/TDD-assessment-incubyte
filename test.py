import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number_returns_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers_returns_sum(self):
        self.assertEqual(self.calculator.add("1,2"), 3)
        self.assertEqual(self.calculator.add("48,55"), 103)
        self.assertEqual(self.calculator.add("33,18"), 51)
        self.assertEqual(self.calculator.add("45,2"), 47)
        self.assertEqual(self.calculator.add("11,2362"), 2373)

    def test_more_than_two_numbers_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,2,3")
        self.assertEqual(str(context.exception), "Cannot process more than two numbers")

if __name__ == '__main__':
    unittest.main()
