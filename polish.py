import unittest

def eval(inputs):
	stack = []
	result = 0
	for i in inputs:
		if i.isdigit():
			stack.insert(0, i)
	return sum(stack)

def parseInput(input):
	if " " not in input:
	    return input
	return eval(input.split(' '))

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(parseInput("1"), "1")

    def testOneSpaceTab(self):
        self.assertEqual(parseInput("1 2"), 3)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
