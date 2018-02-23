import unittest
import math
import operator

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.floordiv,
       '^': operator.pow}

def eval(inputs):
	stack = []
	result = 0
	for i in inputs:
		if i.isdigit():
			stack.insert(0, int(i))
		else:
			a = int(stack.pop(1))
			b = int(stack.pop(0))
			result = ops[i](a, b)
			stack.insert(0, result)
	return result

def parseInput(input):
	if " " not in input:
	    return input
	return eval(input.split(' '))

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(parseInput("1"), "1")

    def testAdd(self):
        self.assertEqual(parseInput("1 2 +"), 3)

    def testSub(self):
        self.assertEqual(parseInput("2 1 -"), 1)

    def testMul(self):
        self.assertEqual(parseInput("1 2 *"), 2)

    def testDiv(self):
        self.assertEqual(parseInput("2 1 /"), 2)

    def testPow(self):
        self.assertEqual(parseInput("2 1 ^"), 2)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
