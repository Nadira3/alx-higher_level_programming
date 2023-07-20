#!/usr/bin/python3

"""
    base test module
"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    """
        TestBase - unittests for the function
    """

    def test_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base("str")
        self.assertEqual(b.id, 'str')
        b = Base(float("inf"))
        self.assertEqual(b.id, float("inf"))
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))
        b = Base({"one": 1, "two": 2, "three": 3})
        self.assertEqual(b.id, {'one': 1, 'two': 2, 'three': 3})
        b = Base(0.5)
        self.assertEqual(b.id, 0.5)
        b = Base(-5)
        self.assertEqual(b.id, -5)
        #b = Base(float("NaN"))
        #self.assertTrue(math.isnan(b.id))
