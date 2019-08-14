# a class="result-image"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

driver.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')

driver.maximize_window()

#we can search our html tag by id or class.
email = driver.find_element_by_xpath('//*[@id="username"]') #username    session_key-login
email.send_keys('tomhankss500@gmail.com')

time.sleep(3)


#we can search our html tag by id or class.
password = driver.find_element_by_xpath('//*[@id="password"]')   # password   session_password-login
password.send_keys('s-p*_GY.ECn\G8k:')

time.sleep(3)


#we can search our html tag by id or class.
login = driver.find_element_by_xpath('//*[@class="btn__primary--large from__button--floating"]')  #class = btn__primary--large from__button--floating        id=btn-primary
login.click()

time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="main-search-box"]')
search.send_keys('python programmer')

time.sleep(3)

button = driver.find_element_by_xpath('//*[@id="global-search"]/fieldset/button')
button.click()

time.sleep(3)

people = driver.find_element_by_xpath('//*[@id="search-types"]/div/ul/li[2]/a')
people.click()

time.sleep(10)

driver.quit()