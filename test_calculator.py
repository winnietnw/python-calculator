import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    
    #add
    def test_add1(self):
        self.assertEqual(self.calc.add(-3, 9), 6)

    def test_add2(self):
        self.assertEqual(self.calc.add(-2, -5), -7)

    #substract
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(8, 4), 4)
    
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(-3, -6), 3)

    #multiply
    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)
    
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(-3, 7), -21)

    #divide
    def test_divide1(self):
        self.assertEqual(self.calc.divide(9, 4), 2)
    
    def test_divide2(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    #modulo
    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)
    
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(6, 4), 2)

if __name__ == '__main__':
    unittest.main()