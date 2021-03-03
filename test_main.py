import unittest
from main import *

#establish 3 testing classes, one for the Menu, one to test the BMI module, and the last to test the retirement module

class TestMenu(unittest.TestCase):
    def test_intro(self):
        expected = "Welcome to the BMI/Savings Program"
        self.assertEqual(intro(),expected)

class TestBMI(unittest.TestCase):
    pass

class TestRetirement(unittest.TestCase):
    pass


if __name__ == '__main__': 
    unittest.main() 