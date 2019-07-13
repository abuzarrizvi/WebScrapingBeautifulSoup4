from selenium import webdriver
from time import sleep



driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.google.com')

# search tag using id

search_bar = driver.find_element_by_name('q')

# input data


search_bar.send_keys('I want to learn web scraping')


# submit the form

search_bar.submit()

sleep(10)

driver.close()
