import requests
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
from selenium import webdriver


#user_agent = UserAgent()

main_url = 'http://codingbat.com/java'
#page = requests.get(main_url,headers={'user-agent':user_agent.chrome})
driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')

#soup = BeautifulSoup(page.content,'lxml')
driver.get(main_url)
soup = BeautifulSoup(driver.page_source,'lxml')

base_url = 'http://codingbat.com'

all_divs = soup.find_all('div',class_='summ')

all_links = [base_url + div.a['href'] for div in all_divs]

question_links = []
for link in all_links:
    driver.get(link)
    inner_soup = BeautifulSoup(driver.page_source,'lxml')
    div = inner_soup.find('div',class_='tabc')
    question_links = [base_url + td.a['href'] for td in div.table.find_all('td')]

print(question_links)
driver.quit()
