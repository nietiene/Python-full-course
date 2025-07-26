# unit testinf is the proccess fo testing small part of code(functions, methods) to make them work correctly
# ensure code does what it supposed to do

import unittest

def add(x, y):
    return x * y

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()