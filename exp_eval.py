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
                b = int(myStack.pop())
                a = int(myStack.pop())
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
        elif token.isnumeric():
            myStack.push(token)
        #Throws error for a wrong input
        else:
            raise PostfixFormatException("Invalid token")

    if myStack.size() == 1:
        return int(myStack.pop())
    else: #This will be called if there are not enough operators for the amount of operands
        raise PostfixFormatException("Too many operands")

#string -> string
#Changes a prefix expression to a postfix expression.
def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    pass


