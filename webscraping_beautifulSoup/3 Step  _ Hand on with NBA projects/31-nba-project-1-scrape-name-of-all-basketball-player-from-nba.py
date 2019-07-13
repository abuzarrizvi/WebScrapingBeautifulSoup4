from selenium import webdriver
from bs4 import BeautifulSoup

# create driver
#driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')


#url = 'http://stats.nba.com/players/?ls=iref:nba:gnav'
url = 'https://stats.nba.com/players/list/'
#https://stats.nba.com/players/list/


# download html page
driver.get(url)

# print (driver.page_source)

# create soup
soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_= 'stats-player-list players-list')

# print (div)

for a in div.find_all('a'):
	print (a.text)

driver.quit()