class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

    #Creates an empty stack with a specified capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0

    #self -> boolean
    #Returns true if the stack is empty, and false if it is not
    def is_empty(self):
        if self.num_items == 0:
            return True
        return False

    #self -> boolean
    #Returns true if stack is full, and false otherwise
    def is_full(self):
        if self.num_items == self.capacity:
            return True
        else:
            return False

    #self, literal -> None
    #Pushes an item onto the stack
    #If stack is already full, raises IndexError
    def push(self, item):
        if self.is_full():
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1


    #self -> literal
    #Pops an item from the stack, removing it and returning its value
    #If the stack is empty, raises IndexError
    def pop(self):
        if self.is_empty():
            raise IndexError
        poppedValue = self.items[self.num_items - 1]
        self.num_items -= 1
        return poppedValue

    #self -> literal
    #Peeks at an item from the top of the stack, returning it's value
    #If the stack is empty, raises IndexError
    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.items[self.num_items - 1]

    #self -> integer
    #Returns the size of the stack
    def size(self):
        return self.num_items