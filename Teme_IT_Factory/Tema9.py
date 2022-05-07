'''
Implementati o clasa Login care sa mosteneasca unittest.TestCase

Gasiti elementele in partea de sus folosind ce selectors doriti voi

setUp()
Initializati driver
Navigati catre https://the-internet.herokuapp.com
Dati click pe Form Authentication

tearDown()
Quit browser
'''

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    FORM_AUTHENTIFICATION = (By.XPATH, '//a[text()="Form Authentication"]')
    USERNAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@class="radius"]')
    H2_BUTTON = (By.XPATH, '//h2')
    ELEMENTAL_BUTTON = (By.XPATH, '//a[text()="Elemental Selenium"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@id="flash"]')
    LOGIN_ERROR = (By.XPATH, '//div[@class="flash error"]')
    CLOSE_ERROR_MESSAGE = (By.XPATH, '//a[@class="close"]')
    LOGOUT_BUTTON = (By.XPATH, '//i[@class="icon-2x icon-signout"]')



    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com')
        self.chrome.implicitly_wait(5)
        self.chrome.find_element(*self.FORM_AUTHENTIFICATION).click()



    def tearDown(self):
        self.chrome.quit()

#Test1
#Verificati ca noul url e corect

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'URL is incorrect')

#Test2
#Verificati ca page title e corect

    def test_page_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

#Test3
#Verificati textul de pe elementul xpath=//h2 e corect

    def test_submit_btn_text(self):
        actual = self.chrome.find_element(*self.H2_BUTTON).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Submit btn text is incorrect')

#Test4
#Verificati ca butonul de login este displayed

    def test_elem_visible(self):
        elem = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(elem.is_displayed(), 'Submit btn nu e vizibil')

#Test5
#Verificati ca atributul href al linkului ‘Elemental Selenium’ e corect

    def test_elem_atribute(self):
        actual = self.chrome.find_element(*self.ELEMENTAL_BUTTON).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'Submit btn href attribute is wrong')

#Test6
#Lasati goale user si pass
#Click login
#Verifica ca eroarea e displayed

    def test_error_display(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = self.chrome.find_element(*self.ERROR_MESSAGE)
        self.assertTrue(error.is_displayed(), 'Error message is not visible')

#Test7
#Completeaza cu user si pass invalide
#Click login
#Verifica ca mesajul de pe eroare e corect
#Este si un x pus acolo extra asa ca vom folosi solutia de mai jos
#expected = 'Your username is invalid!'
#self.assertTrue(expected in actual, 'Error message text is incorrect')

    def test_user_pass_invalide(self):
        self.chrome.find_element(*self.USERNAME).send_keys('abc')
        self.chrome.find_element(*self.PASSWORD).send_keys('123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        print(actual)
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

#Test8
#Lasati goale user si pass
#Click login
#Apasa x la eroare
#Verifica ca eroarea a disparut

    def test_error_message_disappeared(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.CLOSE_ERROR_MESSAGE).click()
        try:
            self.chrome.find_element(*self.LOGIN_ERROR)
        except NoSuchElementException:
            pass

# Test9
# Ia ca o lista toate //label
# Verifica textul ca textul de pe ele sa fie cel asteptat (Username si Password)
# Aici e ok sa avem 2 asserturi


    def test_label_test(self):
        lista_label = self.chrome.find_elements(By.XPATH, '//label')
        actual = (lista_label)[0].text
        expected = 'Username'
        self.assertEqual(actual, expected, "Username label este incorect")
        actual2 = (lista_label)[1].text
        expected2 = 'Password'
        self.assertEqual(actual2, expected2, "Password label este incorect")


#Test10
#Completeaza cu user si pass valide
#Click login
#Verifica ca noul url CONTINE /secure
#Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
#Verifica ca elementul cu clasa=’flash succes’ este displayed
#Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’

    def test_login_flow(self):
        self.chrome.find_element(*self.USERNAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.current_url
        expected = 'secure'
        self.assertTrue(expected in actual, "The link doesn't contains secure")
        try:
            WebDriverWait(self.chrome, 5).\
                until(EC.presence_of_element_located((By.XPATH, '//div[@class="flash success"]')))
        except TimeoutException:
            self.assertTrue\
                (False, "I've been waiting for 5 seconds but I haven't found the element with 'flash success' class")
            elem = self.chrome.find_element(By.XPATH, '//div[@class="flash success"]')
            self.assertTrue(elem.is_displayed(), 'Not the green element')
            actual2 = elem.text
            expected2 = 'secure area'
            self.assertTrue(expected2 in actual2, 'The text of the green elem does NOT contain secure area')

#Test11
#Completeaza cu user si pass valide
#Click login
#Click logout
#Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login

    def test_login_logout(self):
        self.chrome.find_element(*self.USERNAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, "You are NOT in the right place")



