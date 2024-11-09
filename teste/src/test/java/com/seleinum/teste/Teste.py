import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import pyautogui
import pyscreeze


class TesteSelenium(unittest.TestCase):

    def setUp(self):
        # Inicialização do driver chrome
        options = webdriver.ChromeOptions()

        # Maximiza a janela do navegador
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def test_google(self):
        self.driver.get("https://www.google.com.br")
        time.sleep(5)
        self.capturar()

    def capturar(self):
       self.imagem = pyautogui.screenshot()
       self.imagem.save('C:/Users/robso/OneDrive/Documentos/CursoPython/Python/teste/img/'f'screenshot_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png')
   
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
 unittest.main()