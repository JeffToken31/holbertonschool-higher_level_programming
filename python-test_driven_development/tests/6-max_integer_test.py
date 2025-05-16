#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_with_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_with_negativ_integer(self):
        self.assertEqual(max_integer([-1, -2, -3, -400000]), -1)

    def test_with_max_integer(self):
        self.assertEqual(max_integer([4, 5, 10e1000000]), float('inf'))

    def test_with_float(self):
        self.assertEqual(max_integer([1.2, 2.3, 3.45151651651, 4.5]), 4.5)

    def test_with_negatif_float(self):
        self.assertEqual(max_integer([-1.2, -2.3, -3.45151651651, -4.5]), -1.2)

    def test_with_mixed_allowed_type(self):
        self.assertEqual(max_integer([-1.5654, 0x5f, -0b10101110, 0o66]), 95)

    def test_with_str(self):
        self.assertEqual(max_integer(["abc", "bac", "cadadada", "dac"]), "dac")

    def test_with_integer(self):
        self.assertEqual(max_integer([]), "")

    def test_with_empty_tuple(self):
        self.assertEqual(max_integer(()), None)

    def test_with_empty_dict(self):
        self.assertEqual(max_integer({}), None)

    def test_with_empty_str(self):
        self.assertEqual(max_integer([-1, True, False]), True)

    def test_with_integer(self):
        self.assertEqual(max_integer([-1, True, False]), True)

    def test_not_equal(self):
        self.assertNotEqual(max_integer(["a", "b", "c", "d"]), 3)

    def test_with_listinlist(self):
        with self.assertRaises(TypeError):
            max_integer([[1, 2, 4], 2.3, 3.4, 4.5])

    def test_integer_without_list(self):
        with self.assertRaises(TypeError):
            max_integer(1, 5)

    def test_with_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([(1, 2, 4), 2.3, 3.4, 4.5])

    def test_with_dict(self):
        with self.assertRaises(TypeError):
            max_integer([{'hello': 2, 'bonjour': 6}, 2.3, 3.4, 4.5])

    def test_with_None(self):
        with self.assertRaises(TypeError):
            max_integer([-1, 81, None])


if __name__ == '__main__':
    unittest.main()
