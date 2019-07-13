from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')

driver.get('http://python.org')

html_doc  = driver.page_source

soup = BeautifulSoup(html_doc, 'lxml')

#for printing the html page in indented manner
print( soup.prettify())

driver.quit()