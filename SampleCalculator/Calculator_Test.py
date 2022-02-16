# This is our test class
# To test code in our Calculator class we:
    # Import unittest
    # Import the Calculator class from MyCalculator

import unittest
from MyCalculator import Calculator

# In order to perform tests on our code using the CalculatorTest class, our CalculatorTest class has to inherit the TestCase class from unittest. Shown in line 9
class CalculatorTest(unittest.TestCase):

    # Method to test addition of two numbers
    # We test all edge cases i.e when both numbers are negative, when both are positive and when one is positive and the other is negative 
    def test_add_numbers(self):
        self.assertEqual(Calculator.add_numbers(3,4), 7)
        self.assertEqual(Calculator.add_numbers(7, -3), 4)
        self.assertEqual(Calculator.add_numbers(-4,-4), -8)

    # Method to test the difference of two numbers
    # We test all edge cases i.e when both numbers are negative, when both are positive and when one is positive and the other is negative 
    def test_subtract_numbers(self):
        self.assertEqual(Calculator.subtract_numbers(8,5),3)
        self.assertEqual(Calculator.subtract_numbers(-8,-5),-3)
        self.assertEqual(Calculator.subtract_numbers(-8,5),-13)

     # Method to test product of two numbers
    # We test all edge cases i.e when both numbers are negative, when both are positive and when one is positive and the other is negative 
    def test_multiply_numbers(self):
        self.assertEqual(Calculator.multiply_numbers(8,5),40)
        self.assertEqual(Calculator.multiply_numbers(-8,-5),40)
        self.assertEqual(Calculator.multiply_numbers(-8,5),-40)

    # Method to test division of two numbers
    # We test all edge cases i.e when both numbers are negative, when both are positive and when one is positive and the other is negative 
    def test_divide_numbers(self):
        self.assertEqual(Calculator.divide_numbers(18,6),3)
        self.assertEqual(Calculator.divide_numbers(-18,-6),3)
        self.assertEqual(Calculator.divide_numbers(-18,6),-3)



# We have to write this to ensure that we can run our tests successfully. 
if __name__ == "__main__":
    unittest.main()

# To run this file on your terminal type "Your python version" followed by "SampleCalculator/Calculator_Test.py" 
# For my python version I am using this command - python3 SampleCalculator/Calculator_Test.py