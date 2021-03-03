import unittest
from main import *

#establish 3 testing classes, one for the Menu, one to test the BMI module, and the last to test the retirement module

class TestMenu(unittest.TestCase):
    def test_intro(self):
        expected = "Welcome to the BMI/Savings Program"
        
        self.assert(intro(),)

class TestBMI(unittest.TestCase):
    pass

class TestRetirement(unittest.TestCase):
    pass