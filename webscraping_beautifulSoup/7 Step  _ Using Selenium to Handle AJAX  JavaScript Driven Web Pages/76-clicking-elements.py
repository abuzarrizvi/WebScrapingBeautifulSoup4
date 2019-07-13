from selenium import webdriver
from time import sleep



driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')

# open instagram.com -- > url --> https://www.instagram.com

driver.get('https://www.instagram.com')

sleep(5)

login_button = driver.find_element_by_link_text('Log in')

login_button.click()

sleep(5)


driver.close()