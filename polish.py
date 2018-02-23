import unittest
import math
import operator

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv,
       '^': operator.pow}

def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def preventCthulhu(operand, value):
	if operand == '/' and value == 0:
		raise ZeroDivisionError("OMG")

def eval(inputs):
	stack = []
	result = 0
	for i in inputs:
		if isFloat(i):
			stack.insert(0, float(i))
		else:
			a = float(stack.pop(1))
			b = float(stack.pop(0))
			preventCthulhu(ops[i], b)
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

    def testSub(self):
        self.assertEqual(parseInput("1 2 /"), 0.5)

    def test10Div(self):
        self.assertEqual(parseInput("10 2 /"), 5)

    def testDoubleDiv(self):
        self.assertEqual(parseInput("4.2 2 /"), 2.1)

    def testSummonCthulhu(self):
        self.assertRaises(ZeroDivisionError, parseInput, "1 0 /")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
