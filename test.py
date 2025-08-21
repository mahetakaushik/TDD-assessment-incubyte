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
        self.assertEqual(self.calculator.add("11,2362"), 11)

    def test_multiple_numbers_returns_sum(self):
        self.assertEqual(self.calculator.add("1,2,3,4"), 10)
        self.assertEqual(self.calculator.add("48,55,12"), 115)
        self.assertEqual(self.calculator.add("33,18,2"), 53)
        self.assertEqual(self.calculator.add("45,2,3"), 50)
        self.assertEqual(self.calculator.add("11,2362,2"), 13)

    def test_newline_delimiters(self):
        self.assertEqual(self.calculator.add("1\n2"), 3)
        self.assertEqual(self.calculator.add("1\n2,3"), 6)
        self.assertEqual(self.calculator.add("10\n20\n30"), 60)

    def test_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)
        self.assertEqual(self.calculator.add("//|\n1|2|3"), 6)
        self.assertEqual(self.calculator.add("//-\n10-20-30"), 60)
        self.assertEqual(self.calculator.add("//*\n1***2***3"), 6)
        self.assertEqual(self.calculator.add("//abc\n1abc2abcabcabc1001"), 3)

    def test_negative_numbers_throw_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2")
        self.assertEqual(str(context.exception), "negatives not allowed: -2")

        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -2")

        with self.assertRaises(ValueError) as context:
            self.calculator.add("//;\n-1;2;-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -3")

        with self.assertRaises(ValueError) as context:
            self.calculator.add("//*\n-1***2***-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -3")

    def test_numbers_above_1000_ignored(self):
        self.assertEqual(self.calculator.add("2,1001"), 2)
        self.assertEqual(self.calculator.add("1000,1001"), 0)
        self.assertEqual(self.calculator.add("1\n2,1001"), 3)
        self.assertEqual(self.calculator.add("//;\n13;1001;2"), 15)

if __name__ == '__main__':
    unittest.main()
