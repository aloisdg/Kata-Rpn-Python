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

class TestRpn(unittest.TestCase):

    def testOne(self):
        self.assertEqual(parseInput("1"), "1")

    def testAdd(self):
        self.assertEqual(parseInput("1 2 +"), 3)

    def testSub(self):
        self.assertEqual(parseInput("2 1 -"), 1)

    def testSubZero(self):
        self.assertEqual(parseInput("1 2 -"), -1)

    def testMul(self):
        self.assertEqual(parseInput("1 2 *"), 2)

    def testDiv(self):
        self.assertEqual(parseInput("2 1 /"), 2)

    def testPow(self):
        self.assertEqual(parseInput("2 1 ^"), 2)

    def testAddSub(self):
        self.assertEqual(parseInput("2 1 + 3 -"), 0)

    def testRpn(self):
        self.assertEqual(parseInput("6 4 5 + * 25 2 3 + / -"), 49)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
