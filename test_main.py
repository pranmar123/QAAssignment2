import unittest
from main import *

#establish two different classes for tests: one to test the BMI module, and the last to test the retirement module

class TestBMICalculator(unittest.TestCase):
    def testNormalweightParameters(self):
        actualValue, actualCategory = bmiCalculator("5,3", "125")
        expectedValue, expectedCategory = 22.7, "Normal weight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testUnderweightParameters(self):
        actualValue, actualCategory = bmiCalculator("5,3", "50")
        expectedValue, expectedCategory = 22.7, "Underweight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testOverweightParameters(self):
        actualValue, actualCategory = bmiCalculator("5,3", "50")
        expectedValue, expectedCategory = 22.7, "Underweight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testObeseParameters(self):
        actualValue, actualCategory = bmiCalculator("5,3", "50")
        expectedValue, expectedCategory = 22.7, "Underweight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testInvalidHeight(self):
        actualValue, actualCategory = bmiCalculator("FiveThree", "200")
        expectedValue, expectedCategory = -1, "-1"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testInvalidWeight(self):
        actualValue, actualCategory = bmiCalculator("5,3", "Three")
        expectedValue, expectedCategory = -1, "-1"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)
    



class TestRetirementCalculator(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
