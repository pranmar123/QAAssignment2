import unittest
from processes import *

#Our web application can be found here: https://qa3-4-310802.uc.r.appspot.com/
#establish two different classes for tests: one to test the BMI module, and the last to test the retirement module

class TestBMICalculator(unittest.TestCase):
    def testNormalweightParameters(self):
        actualValue = bmiCalculator("5","3", "125")
        actualCategory = category(22.7)
        expectedValue, expectedCategory = 22.7, "Normal weight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testUnderweightParameters(self):
        actualValue= bmiCalculator("5","3", "100")
        actualCategory = category(18.1)
        expectedValue, expectedCategory = 18.1, "Underweight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testOverweightParameters(self):
        actualValue = bmiCalculator("5", "3", "150")
        actualCategory = category(27.2)
        expectedValue, expectedCategory = 27.2, "Overweight"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testObeseParameters(self):
        actualValue = bmiCalculator("5", "3", "200")
        actualCategory = category(36.3)
        expectedValue, expectedCategory = 36.3, "Obese"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testInvalidHeight(self):
        actualValue = bmiCalculator("Five", "Three", "200")
        actualCategory = category(-1)
        expectedValue, expectedCategory = -1, "-1"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testInvalidWeight(self):
        actualValue = bmiCalculator("5", "three", "Three")
        actualCategory = category(-1)
        expectedValue, expectedCategory = -1, "-1"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)

    def testNegativeWeight(self):
        actualValue = bmiCalculator("5", "3", "-20")
        actualCategory = category(-1)
        expectedValue, expectedCategory = -1, "-1"
        self.assertEqual(actualValue,expectedValue)
        self.assertEqual(actualCategory,expectedCategory)
    
    def testNegativeHeight(self):
        actualValue = bmiCalculator("-1", "-3", "-20")
        actualCategory = category(-1)
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
