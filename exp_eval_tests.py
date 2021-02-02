# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    def test_postfix_eval_05(self):
        #Tests +
        self.assertEqual(postfix_eval("3 5.4 +"), 8.4)
        #Tests -
        self.assertEqual(postfix_eval("3.5 5 -"), -1.5)
        #Tests *
        self.assertEqual(postfix_eval("4 2 *"), 8)
        #Tests /
        self.assertEqual(postfix_eval("4 2 /"), 2)
        #Tests **
        self.assertEqual(postfix_eval("4 2 **"), 16)
        #Tests >>
        self.assertEqual(postfix_eval("10 1 >>"), 5)
        #Tests <<
        self.assertEqual(postfix_eval("4 3 <<"), 32)
        #Test division by 0
        try:
            postfix_eval("5 3 3 - /")
            self.fail()
        except ValueError as e:
            self.assertEqual(str(e), "Division by Zero")
    
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* + 3 4 - 2 1"), "3 4 + 2 1 - *")
        self.assertEqual(prefix_to_postfix("* + 3.1 4.4 - 2.93 1"), "3.1 4.4 + 2.93 1 - *")
    
    def test_prefix_to_postfix_error_1(self):
        try:
            prefix_to_postfix("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_prefix_to_postfix_error_2(self):
        try:
            prefix_to_postfix("+ 4")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")


    def test_prefix_to_postfix_error_3(self):
        try:
            prefix_to_postfix("+ 1 2 3")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

if __name__ == "__main__":
    unittest.main()
