# coding: utf-8
# div class="listings-container"

# 	div class=listing-card-wrapper

# 		titile --> span class="listing-name--display"
# 		price --> span class="price-amount"
# 		guest --> span class="person-capacity"
# 		reviews --> get all span inside block and get the final

from selenium import webdriver
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')


url = 'https://www.airbnb.com/s/New-York--NY--United-States?checkin=09%2F13%2F2016&checkout=09%2F15%2F2016&guests=1&zoom=12&search_by_map=true&sw_lat=40.628328897408736&sw_lng=-74.21733629193693&ne_lat=40.806739059800066&ne_lng=-74.07588731732756&ss_id=puaxgepi&page=1&source=map&airbnb_plus_only=false&s_tag=y8aSVLPW'

#driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

div1 = soup.find('div', class_ = 'listings-container')

for div2 in div1.find_all('div', class_ = 'listing-card-wrapper'):

	title_span = div2.find('span', class_ = 'listing-name--display')
	print title_span.text

	price_span = div2.find('span', class_ = 'price-amount')
	print price_span.text

	guest_span = div2.find('span', class_ = 'person-capacity')
	print guest_span.text.strip(' · ')

	if 'reviews' in div2.text:
		review_span = div2.find_all('span')[len(div2.find_all('span')) - 1]
		print review_span.text



driver.quit()
