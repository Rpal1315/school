import unittest
targ = __import__("List_Programs/list_programs.py")
inst = targ.list_insert

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = inst([0,1,3],2,1)
        self.assertEqual(result, [0,1,2,3])  # add assertion here


if __name__ == '__main__':
    unittest.main()
