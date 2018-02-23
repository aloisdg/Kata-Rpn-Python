import unittest

def parseInput(input):
	if " " not in input:
	    return input
	return input

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(parseInput("1"), "1")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
