import unittest
from simple_test import summarize,get_info 

class TestMain(unittest.TestCase):
    def test_summarize1(self):
        # Arrange
        a = 5
        b = 6
        excepted = 12
        # Act
        result = summarize(a, b)
        # Assertions
        self.assertEqual(excepted,result)

    def test_summarize2(self):
        a = -5
        b = 7
        excepted = 2
        result = summarize(a, b)
        self.assertEqual(excepted,result)

    def test_summarize3(self):
        a = 5
        b = -7
        excepted = -2
        result = summarize(a, b)
        self.assertEqual(excepted,result)        