
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class Calculadora:
    def __init__(self, driver):
        self.driver = driver
        self.num1 = WebDriverWait(self.driver.instance, 15).until(
            EC.presence_of_element_located((MobileBy.ID, 'com.google.android.calculator:id/digit_1')))
        self.num2 = WebDriverWait(self.driver.instance, 15).until(
            EC.presence_of_element_located((MobileBy.ID, 'com.google.android.calculator:id/digit_2')))
        self.display = WebDriverWait(self.driver.instance, 15).until(
            EC.presence_of_element_located((MobileBy.ID, 'com.google.android.calculator:id/formula')))
        self.soma = WebDriverWait(self.driver.instance, 15).until(
            EC.presence_of_element_located((MobileBy.ID, 'com.google.android.calculator:id/op_add')))
        self.subtrair = WebDriverWait(self.driver.instance, 15).until(
            EC.presence_of_element_located((MobileBy.ID, 'com.google.android.calculator:id/op_sub')))
        self.multiplicar = WebDriverWait(self.driver.instance, 15).until(
            EC.presence_of_element_located((MobileBy.ID, 'com.google.android.calculator:id/op_mul')))
        self.dividir = WebDriverWait(self.driver.instance, 15).until(
            EC.presence_of_element_located((MobileBy.ID, 'com.google.android.calculator:id/op_div')))
        self.igual = WebDriverWait(self.driver.instance, 15).until(
            EC.presence_of_element_located((MobileBy.ID, 'com.google.android.calculator:id/eq')))

    def clicarnumero(self, numero):
        _num = str(numero)
        self.driver.instance.find_element(
            MobileBy.ID, 'com.google.android.calculator:id/digit_' + _num).click()

    def somando(self, num1, num2):
        self.clicarnumero(num1)
        self.soma.click()
        self.clicarnumero(num2)
        self.igual.click()

        resultado = num1 + num2
        calcularResultado = int(self.display.text)
        assert resultado == calcularResultado, 'Resultados Diferentes'

    def subtraindo(self, num1, num2):
        self.clicarnumero(num1)
        self.subtrair.click()
        self.clicarnumero(num2)
        self.igual.click()

        resultado = num1 - num2
        calcularResultado = int(self.display.text)
        assert resultado == calcularResultado, 'Resultados Diferentes'

    def multiplicando(self, num1, num2):
        self.clicarnumero(num1)
        self.multiplicar.click()
        self.clicarnumero(num2)
        self.igual.click()

        resultado = num1 * num2
        calcularResultado = int(self.display.text)
        assert resultado == calcularResultado, 'Resultados Diferentes'

    def dividindo(self, num1, num2):
        self.clicarnumero(num1)
        self.dividir.click()
        self.clicarnumero(num2)
        self.igual.click()

        resultado = num1 / num2
        calcularResultado = int(self.display.text)
        assert resultado == calcularResultado, 'Resultados Diferentes'
