"""
Reverse Polish Notation

input可以是double，返回也是double，然后不保证input valid。
需要自己写error handling。然后followup问如果有很多别的运算符，类似根号啥的
"""

import math
from abc import ABCMeta, abstractmethod

class Expression(object, metaclass=ABCMeta):

    @abstractmethod
    def calculate(self, left, token, right=None):
        pass


class TwoOpsExp(Expression):

    def calculate(self, left, token, right=None):
        if token == "+":
            return left + right
        elif token == "-":
            return left - right
        elif token == "*":
            return left * right
        elif token == "/":
            if right == 0:
                print("ZeroDivisionError: division by zero")
                return 0
            return left / right
        elif token == "%":
            if right == 0:
                print("ZeroDivisionError: integer division or modulo by zero")
            return left % right
        else:
            print("Invalid operator  ", token) 
            return 0



class OneOpsExp(Expression):

    def calculate(self, left, token, right=None):
        if token == "sqrt":
            return math.sqrt(left)
        elif token == "square":
            return left * left
        else:
            print("others...")
            return left



class Solution:
    def __init__(self):
        self.two_operands = ["+", "-", "*", "/", "%"]
        self.one_operands = ["sqrt", "square", "others..."]


    def evalRPN(self, tokens):
        stack = []
        two_exp = TwoOpsExp()
        one_exp = OneOpsExp()
        for idx, token in enumerate(tokens):
            if token not in self.two_operands and token not in self.one_operands:
                stack.append(token)
            else:
                if token in self.two_operands:
                    if len(stack) < 2:
                        print("Invalid expression")
                        return 0
                    right = stack.pop()
                    left = stack.pop()
                    
                    tmp = two_exp.calculate(float(left), token, float(right))
                    stack.append(str(tmp))

                elif token in self.one_operands:
                    if len(stack) < 1:
                        print("Invalid expression")
                        return 0
                    left = stack.pop()

                    tmp = one_exp.calculate(float(left), token)
                    stack.append(str(tmp))

        if not stack or len(stack) > 1:
            print("Invalid expression")
            return 0

        print(stack[-1])

solver = Solution()
solver.evalRPN(["+","-","5"])
solver.evalRPN(["23","3","5"])
solver.evalRPN(["23","0","/"])
solver.evalRPN(["23","0","sqrt"])
solver.evalRPN(["23","0","sqrt", "square", "+"])
solver.evalRPN(["23","0","sqrt", "square", "+", "/"])

