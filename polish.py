import unittest

def eval(input):
	return input

def parseInput(input):
	if " " not in input:
	    return input
	return eval(input.split(' ')[0])

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(parseInput("1"), "1")

    def testOneSpace(self):
        self.assertEqual(parseInput("1 2"), "1")

    def testOneSpace(self):
        self.assertEqual(parseInput("1 2"), "1")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
