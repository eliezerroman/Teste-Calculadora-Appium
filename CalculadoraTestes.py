import unittest
from Calc import Calculadora
from Webdriver import Driver


class CalculadoraTestes(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_soma(self):
        calculadora = Calculadora(self.driver)
        calculadora.somando(2, 5)

    def test_multiplicando(self):
        calculadora = Calculadora(self.driver)
        calculadora.multiplicando(3, 4)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
