#https://www.phptravels.net/
#http://automationpractice.com/index.php
#https://formy-project.herokuapp.com/
#https://the-internet.herokuapp.com/
#https://www.techlistic.com/p/selenium-practice-form.html
#jules.app

#3 selectors by:
#Id
#Link text
#Partial link text
#Name
#Tag*
#Class name*
#Css (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)

#*La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista

#La Xpath:
#3 dupa atribut valoare
#3 dupa textul de pe element
#1 dupa partial text
#1 cu SAU, folosind pipe |
#1 cu *
#1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
#1 in care sa folosesti parent::
#1 in care sa folosesti fratele anterior sau de dupa (la alegere)
#1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.


#1. ID
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('http://automationpractice.com/index.php')

first_name = chrome.find_element(By.ID, 'search_query_top')
first_name.send_keys('Dress')


sleep(3)
chrome.quit()

#2. LinkText

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/')

chrome.find_element(By.LINK_TEXT, 'Dropdown').click()

sleep(3)
chrome.quit()


#3. Partial_LinkText

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/')

chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()

sleep(3)
chrome.quit()

#4. CSS

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/autocomplete')

chrome.find_element(By.CSS_SELECTOR,'input#autocomplete' ).send_keys('Bistrita-')

chrome.find_element(By.CSS_SELECTOR,'input.form-control').send_keys('Nasaud')

chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Street address"]' ).send_keys('Crinilor')


sleep(3)
chrome.quit()


# 5. Xpath

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/form')

chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('Andreea')

chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('Morariu')

chrome.find_element(By.XPATH,'input[@placeholder="Enter your job title"]').send_keys('Tester')

sleep(3)
chrome.quit()


chrome.get('http://automationpractice.com/index.php')
chrome.find_element(By.XPATH,'//a[text()="Popular"]').click()
chrome.find_element(By.XPATH,'//a[text()="Best Sellers"]').click()

sleep(3)
chrome.quit()




