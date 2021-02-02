from stack_array import Stack
import math

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

#string -> int
#Evaluates a postfix expression. Throw error if there are too many or not enough expression
def postfix_eval(input_str):
    input_list = str.split(input_str)
    myStack = Stack(len(input_list))

    for token in input_list:
        #Handles using the operator on the top two values in the stack
        if token in ["+", "-", "*", "/", "**", ">>", "<<"]:
            if myStack.size() >= 2:
                b = myStack.pop()
                a = myStack.pop()

                #Casts the strings to an int or float, depending on what it is
                try:
                    b = int(b)
                except:
                    b = float(b)
                
                try:
                    a = int(a)
                except:
                    a = float(a)

                if token == "+":
                    myStack.push(a + b)
                elif token == "-":
                    myStack.push(a - b)
                elif token == "*":
                    myStack.push(a * b)
                elif token == "/":
                    myStack.push(a / b)
                elif token == "**":
                    myStack.push(a ** b)
                elif token == ">>":
                    myStack.push(a >> b)
                elif token == "<<":
                    myStack.push(a << b)
            else: #This will be called if the stack does not have enough operands to use the operator on
                raise PostfixFormatException("Insufficient operands")
        #Handles adding a number to the stack
        elif isIntOrFloat(token):
            myStack.push(token)
        #Throws error for a wrong input
        else:
            raise PostfixFormatException("Invalid token")

    if myStack.size() == 1:
        return myStack.pop()
    else: #This will be called if there are not enough operators for the amount of operands
        raise PostfixFormatException("Too many operands")

#string -> string
#Changes a prefix expression to a postfix expression.
def prefix_to_postfix(input_str):
    input_list = str.split(input_str)
    input_list.reverse()
    myStack = Stack(len(input_list))

    for token in input_list:
        #Handles operators
        if token in ["+", "-", "*", "/", "**", ">>", "<<"]:
            if myStack.size() >= 2:
                firstOperand = myStack.pop()
                secondOperand = myStack.pop()
                myStack.push(firstOperand + " " + secondOperand + " " + token)
            #Throws an error if the stack does not have enough operands to combine with the operator
            else:
                raise PostfixFormatException("Insufficient operands")
        #Handles operands
        elif isIntOrFloat(token):
            myStack.push(token)
        #Throws an error if a token is not an operator or a operand
        else:
            raise PostfixFormatException("Invalid token")
    
    if myStack.size() == 1:
        return myStack.pop()
    #Throws an error if there aren't enough operators for the given operands
    else:
        raise PostfixFormatException("Too many operands")

#String -> boolean
#Helper function that returns true if the token is a float or an int.
def isIntOrFloat(token):
    if token.isnumeric():
        return True
    else:
        try:
            token = float(token)
            return True
        except:
            return False