import unittest
from fib import fib, fib2


class MyTestCase(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(100), '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ')

    def test_fib2(self):
        self.assertEqual(fib2(11), 89)


if __name__ == '__main__':
    unittest.main()
