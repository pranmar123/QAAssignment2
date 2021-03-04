import unittest
from main import *

#establish two different classes for tests: one to test the BMI module, and the last to test the retirement module

class TestBMI(unittest.TestCase):
    def testBMICalculatorWithNormalParameters(self):
        actualValue, actualCategory = bmiCalculator("5 3",125)
        expectedValue, expectedCategory = 22.7, "Normal weight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

class TestRetirement(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
