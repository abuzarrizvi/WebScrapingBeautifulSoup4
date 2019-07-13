# Height:
# Weight:
# Born:

from selenium import webdriver
from bs4 import BeautifulSoup

#driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
url = 'http://www.nba.com/playerfile/tony_allen/'

driver.get(url)

# print driver.page_source

soup = BeautifulSoup(driver.page_source, 'lxml')

Height = ""

h_span = soup.find('span', string = 'Height:')

for span in h_span.findNextSiblings():
	Height = Height + span.text


Weight = ""

w_span = soup.find('span', string = 'Weight:')

for span in w_span.findNextSiblings():
	Weight = Weight + span.text


Born = ""

b_span = soup.find('span', string = 'Born:')

for span in b_span.findNextSiblings():
	Born = Born + span.text

print( Height)
print (Weight)
print (Born)

driver.quit()
