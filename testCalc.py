import calculator
import math
import unittest

class testCaseCalculator(unittest.TestCase):
    def test_calculator(self):
        print(" === Testing PASS CASES ===")
        print("")
        print("testing 10 + 5")
        add = calculator.addition(10, 5)
        print(add)
        self.assertEqual(add, 15)

        print("")
        print("testing 10 - 5")
        subtract = calculator.subtraction(10,5)
        print(subtract)
        self.assertEqual(subtract, 5)

        print("")
        print("testing 10 * 5")
        multiply = calculator.multiplication(10,5)
        print(multiply)
        self.assertEqual(multiply, 50)

        print("")
        print("testing 10 / 5")
        divide = calculator.division(10,5)
        print(divide)
        self.assertEqual(divide, 2)

        print("")
        print(" === TESTING FAILED TESTS ===")
        print("")
        print("testing 15 * cheese")
        multiply2 = calculator.multiplication(15,"cheese")
        print(multiply2)
        self.assertEqual(multiply2, 0)

        print("")
        print("testing 10 / 0")
        divide2 = calculator.division(10,0)
        print(divide2)
        self.assertEqual(divide2, 2)

if __name__ == '__main__':
    unittest.main()