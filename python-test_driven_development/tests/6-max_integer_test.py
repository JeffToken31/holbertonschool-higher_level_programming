#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer_with_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_with_negativ_integer(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_with_float(self):
        self.assertEqual(max_integer([1.2, 2.3, 3.4, 4.5]), 4.5)
        self.assertEqual(max_integer([float('inf'), 2.3]), float('inf'))

    def test_max_integer_with_str(self):
        with self.assertRaises(TypeError):
            max_integer([[1, 2], 2.3, 3.4, 4.5]), 4.5


if __name__ == '__main__':
    unittest.main()
