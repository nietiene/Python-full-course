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
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()