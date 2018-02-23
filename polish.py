import unittest

def parseIntput(input):
	return input;

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(parseInput(1), 1)

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
