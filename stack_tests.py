import unittest

#Submit with linked stack commented out
from stack_array import Stack
#from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(3)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.peek(), 0)
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.size(),3)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.peek(), 0)
        self.assertEqual(stack.size(),1)
        self.assertEqual(stack.pop(), 0)
        self.assertEqual(stack.size(),0)

    def test_EmptyAndFull(self):
        stack = Stack(1)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push(5)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())

    def test_NoneAsData(self):
        stack = Stack(3)
        stack.push(None)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertEqual(stack.size(), 0)
    
    def test_Errors(self):
        stack = Stack(1)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push(1)
        with self.assertRaises(IndexError):
            stack.push(2)



if __name__ == '__main__': 
    unittest.main()