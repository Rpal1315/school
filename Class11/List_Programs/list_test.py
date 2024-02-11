import unittest

from list_programs import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = list_presence([0, 1, 2, 3, 4, 5], 2)
        result1 = list_presence([0, 1, 2, 3, 4, 5], 6)
        self.assertEqual(result, True)  # add assertion here
        self.assertEqual(result1,False)
    def test_something1(self):
if __name__ == '__main__':
    unittest.main()
