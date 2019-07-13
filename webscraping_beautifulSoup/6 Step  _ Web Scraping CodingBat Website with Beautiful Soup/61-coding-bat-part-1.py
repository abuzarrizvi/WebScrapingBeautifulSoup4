import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
main_url = 'http://codingbat.com/java'
driver.get(main_url,)
soup = BeautifulSoup(driver.page_source,'lxml')

base_url = 'http://codingbat.com'

all_divs = soup.find_all('div',class_='summ')

for div in all_divs:
    print(base_url + div.a['href'])
driver.quit()