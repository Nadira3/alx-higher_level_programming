#!/usr/bin/python3

"""
    Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        TestMaxInteger - unittests for the function
        def max_integer(list=[])
    """

    def test_default(self):
        self.assertEqual(max_integer(), None)

    def test_noarg(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 2, 3, -2, -1]), 3)
        self.assertEqual(max_integer([-1, 0, -3, -2, -1]), 0)
        self.assertEqual(max_integer([-1, -6, -3, -2, -4]), -1)
 
    def test_other(self):
        with self.assertRaises(TypeError):
            max_integer("string")
            max_integer(12)
            max_integer((1, 2, 3))
            max_integer({"one": 1, "two": 2, "three": 3})
            max_integer([3, 0, (3, 5), 8, "str"])
            max_integer([3, 0, "a", 8, "str"])
