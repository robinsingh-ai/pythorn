"""
Author : Robin Singh

Programs List:

1.Stack

2.Infix To Postfix Conversion Using Stack

3.Integer To Binary Conversion Using Stack
"""

import inspect


class Stack(object):

    """
    Stack implementation
    """

    def __init__(self):
        """
        :param  items: Empty Array
        """
        self.items = []

    def push(self, item):
        """
        Pushes an item into the array 
        """
        self.items.append(item)

    def pop(self):
        """
        Pops the top element from the stack, and return -1 if the stack is empty
        """
        if self.items == []:
            # We can also return true here
            return -1
        else:
            # Returns popped element
            return self.items.pop()

    def tos(self):
        """
        returns the top element of the stack, else return -1 if stack is empty
        """
        if self.items:
            return self.items[-1]
        else:
            return -1

    def size(self):
        """
        returns the length of the stack, else returns -1 if stack is empty
        """
        if self.items:
            return len(self.items)
        else:
            return -1

    def isEmpty(self):
        """
        checks if the stack is empty or not and returns boolean value
        """
        if self.items == []:
            return True
        else:
            return False

    def display(self):
        """
        if there is an element in the stack then it prints the full stack ,else  returns -1 
        """
        if self.items == []:
            return -1
        else:
            print(self.items)

    @staticmethod
    def get_code():
        """
        :return: source code
        """
        return inspect.getsource(Stack)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return "push(), pop(), isEmpty() ,display() ,size() and tos() all take O(1) time. We do not run any loop in any of these operations"


class Infix_Postfix(object):
    """
    Infix To Postfix conversion
    """

    def __init__(self, expression=None, stack=None):
        """
        : param expression: the infix expression which we are passing here to convert to postfix exp.
        : param stack: stack class function to perform basic operations in stack
        """
        self.Exp = list(expression)
        self.stack = stack

    @staticmethod
    def oper(char):
        """
        Function of checking whether the given character is an operator or not.
        """

        return (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z'))

    @staticmethod
    def _pr(char):
        """
        Function of checking precedence for the given character
        """
        if char == '+' or char == '-':
            return 1
        elif char == '*' or char == '/':
            return 2
        elif char == '^':
            return 3
        else:
            return -1

    def infixToPostfix(self):
        """
        main function for converting infix to postfix using stack.

        :return: converted expression
        """
        postFix = []
        for i in range(len(self.Exp)):
            if (self.oper(self.Exp[i])):
                postFix.append(self.Exp[i])

            elif(self.Exp[i] == '('):
                self.stack.push(self.Exp[i])

            elif(self.Exp[i] == ')'):
                top = self.stack.pop()

                while(not self.stack.isEmpty() and top != '('):
                    postFix.append(top)
                    top = self.stack.pop()

            else:
                while (not self.stack.isEmpty()) and (self._pr(self.Exp[i]) <= self._pr(self.stack.tos())):
                    postFix.append(self.stack.pop())
                self.stack.push(self.Exp[i])

        while(not self.stack.isEmpty()):
            postFix.append(self.stack.pop())

        return ' '.join(postFix)

    @staticmethod
    def get_code():
        """
        :return: source code 
        """
        return inspect.getsource(Infix_Postfix)



class Integer_Binary(object):
    """
    Integer To Binary Conversion
    """

    def __init__(self, Number=None, stack=None):
        """
        :param number: number to convert to binary
        :param stack: stack class function to perform basic operations in stack
        """
        self.number = Number
        self.stack = stack

    def IntegerBinary(self):

        while self.number > 0:
            remainder = self.number % 2
            self.stack.push(remainder)
            self.number = self.number // 2

        binaryConv = ""
        while not self.stack.isEmpty():
            binaryConv += str(self.stack.pop())

        return binaryConv

    @staticmethod
    def get_code():
        """
        :return: source code        
        """
