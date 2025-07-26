# unit testing is the proccess fo testing small part of code(functions, methods) to make them work correctly
# ensure code does what it supposed to do

import unittest
# unittest module provide tool allows to writing test and run test easily

def add(x, y):
    return x + y

# define test class
# unittset.testCase gives access to testing methood
class TestMath(unittest.TestCase):

    def test_add(self):
        # here it test if 2 + 3 is equat to five if true return OK
        self.assertEqual(add(2, 3), 5)

# this runs test in this file
if __name__ == '__main__':
    unittest.main()

"""
common assetion methoods in unittest
   assertEqual(a, b) -> checks if a == b
   assertNotEqual(a, b) -> checks if a != b
   assertTrue(x) -> checks if bool(x) True
   assertFalse(x) -> ckeck if bool(x) is False
   assertRaises(Error) -> error is raised
"""


# Example with raiseError

def divide(x, y):
    return x / y

class Test(unittest.TestCase):
    def testing(self):
        # with runs the code inside and the checks if exception is raised
        # automatically catch exception if raised
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)