'''
Create a simple calculator that given a string of operators (), +, -, *, / 
and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Remember about the order of operations!
Multiplications and divisions have a higher priority and should be performed left-to-right. 
Additions and subtractions have a lower priority and should also be performed left-to-right.
'''

class Calculator(object):
	e = eval
	@staticmethod
	def evaluate(string):
		return e(string)