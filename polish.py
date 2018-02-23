import unittest

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

def DivideByTwo(n):
    if (n == 0):
        raise ValueError("Zero")
    return n / 2

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testTwo(self):
        self.assertFalse(IsOdd(2))

    def testException(self):
        self.assertRaises(ValueError, DivideByTwo, 0)

    def test(self):
        self.assertEqual(1, DivideByTwo(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
