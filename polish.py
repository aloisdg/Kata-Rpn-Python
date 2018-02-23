import unittest

def eval(input):
	stack = []
	result = 0
	return result

def parseInput(input):
	if " " not in input:
	    return input
	return eval(input.split(' '))

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(parseInput("1"), "1")

    def testOneSpaceTab(self):
        self.assertEqual(parseInput("1 2"), 0)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
