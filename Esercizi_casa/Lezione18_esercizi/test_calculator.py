import unittest
from calculator import calculate, FormulaError

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("1 + 1"), 2.0)
    
    def test_subtraction(self):
        self.assertEqual(calculate("4 - 2"), 2.0)
    
    def test_invalid_operator(self):
        with self.assertRaises(FormulaError):
            calculate("2 * 2")
    
    def test_non_numeric_operand(self):
        with self.assertRaises(FormulaError):
            calculate("two + 2")
    
    def test_incorrect_format(self):
        with self.assertRaises(FormulaError):
            calculate("1 +")
    
    def test_empty_input(self):
        with self.assertRaises(FormulaError):
            calculate("")
    
    def test_whitespace_input(self):
        with self.assertRaises(FormulaError):
            calculate("    ")

    def test_large_numbers(self):
        self.assertEqual(calculate("1000000000 + 1000000000"), 2000000000.0)
    
    def test_negative_numbers(self):
        self.assertEqual(calculate("-1 - -1"), 0.0)
    
    def test_float_numbers(self):
        self.assertEqual(calculate("1.5 + 2.5"), 4.0)


if __name__ == "__main__":
    unittest.main()