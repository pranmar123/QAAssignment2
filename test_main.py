import unittest
from main import *

#Our web application can be found here: https://qa3-4-310802.uc.r.appspot.com/
#establish two different classes for tests: one to test the BMI module, and the last to test the retirement module

class TestBMICalculator(unittest.TestCase):
    def testNormalweightParameters(self):
        actualValue, actualCategory = bmiCalculator("5,3", "125")
        expectedValue, expectedCategory = 22.7, "Normal weight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testUnderweightParameters(self):
        actualValue, actualCategory = bmiCalculator("5,3", "100")
        expectedValue, expectedCategory = 18.1, "Underweight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testOverweightParameters(self):
        actualValue, actualCategory = bmiCalculator("5,3", "150")
        expectedValue, expectedCategory = 27.2, "Overweight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testObeseParameters(self):
        actualValue, actualCategory = bmiCalculator("5,3", "200")
        expectedValue, expectedCategory = 36.3, "Obese"
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

    def testNegativeWeight(self):
        actualValue, actualCategory = bmiCalculator("5,3", "-20")
        expectedValue, expectedCategory = -1, "-1"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)
    
    def testNegativeHeight(self):
        actualValue, actualCategory = bmiCalculator("-1,-3", "-20")
        expectedValue, expectedCategory = -1, "-1"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)
    
    



class TestRetirementCalculator(unittest.TestCase):
    def testRetirementWithNormalParameters(self):
        actual = retirementCalculator("24","100000","10","1000000")
        expected = 98
        self.assertEqual(actual,expected)
    
    def testRetirementWithYoungKidParameters(self):
        actual = retirementCalculator("10","1000","90","10000")
        expected = 18
        self.assertEqual(actual,expected)

    def testRetirementWithNormalParametersWithMoneyCommas(self):
        actual = retirementCalculator("24","100,000","10","1,000,000")
        expected = 98
        self.assertEqual(actual,expected)

    def testRetirementWithGoalReachInTheSameYear(self):
        actual = retirementCalculator("24","100,000","100","100,000")
        expected = 24
        self.assertEqual(actual,expected)
    
    def testRetirementGoalNotMet(self):
        actual = retirementCalculator("24","100,000","10","100,000,000")
        expected = -1
        self.assertEqual(actual,expected)
    
    def testRetirementWithNonNumberParameters(self):
        actual = retirementCalculator("Twenty","#(#),000","&","100,000,000")
        expected = -1
        self.assertEqual(actual,expected)

    def testRetirementAgeBeingNegative(self):
        actual = retirementCalculator("-24","100,000","10","100,000,000")
        expected = -1
        self.assertEqual(actual,expected)     

    def testRetirementSalaryBeingNegative(self):
        actual = retirementCalculator("24","-100,000","10","100,000,000")
        expected = -1
        self.assertEqual(actual,expected)  
    
    def testRetirementGoalBeingNegative(self):
        actual = retirementCalculator("24","-100,000","10","-1000")
        expected = -1
        self.assertEqual(actual,expected)  

    def testRetirementPercentGreaterThan100(self):
        actual = retirementCalculator("24","100,000","120","100,000,000")
        expected = -1
        self.assertEqual(actual,expected)     


if __name__ == '__main__':
    unittest.main()
