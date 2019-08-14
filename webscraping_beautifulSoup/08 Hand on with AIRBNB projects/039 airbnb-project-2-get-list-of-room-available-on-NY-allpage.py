# coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

class Room():
	"""docstring for Room"""
	def __init__(self):
		self.title = ""
		self.price = ""
		self.guests = ""
		self.review = ""
		

def get_all_room_all_page():

	room_list = []

	url = 'https://www.airbnb.com/s/New-York--NY?guests=2&checkin=09%2F09%2F2016&checkout=09%2F15%2F2016&search_by_map=true&sw_lng=-74.15053101169235&sw_lat=40.28249032559194&ne_lng=-73.15077515231735&ne_lat=41.132524449471795&zoom=10&ss_id=fc6429hj&ss_preload=true&source=bb&s_tag=PGDH1Zuz'

	#driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
	driver.get(url)

	soup = BeautifulSoup(driver.page_source,'lxml')

	# get number of pages
	div_paging = soup.find('div', class_ = 'pagination')

	page_num = int(div_paging.find_all('li')[len(div_paging.find_all('li')) - 2].text)

	print page_num

	for page in range(1,page_num + 1):
		
		new_url = url + '&page={0}'.format(page)

		driver.get(new_url)

		soup = BeautifulSoup(driver.page_source,'lxml')

		div = soup.find('div',class_ = 'listings-container')

		for s_div in div.find_all('div', class_ = 'listing-card-wrapper'):
			
			print s_div.find('span', class_='listing-name--display').text
			print s_div.find('span', class_ = 'price-amount').text
			print s_div.find('span', class_ = 'person-capacity').text.strip(' · ')
			if 'reviews' in s_div.text:
				# get the final span tag
				print s_div.find_all('span')[len(s_div.find_all('span')) - 1].text
			print '\n'

			room = Room()

			room.title = s_div.find('span', class_='listing-name--display').text
			room.price = s_div.find('span', class_ = 'price-amount').text
			room.guests = s_div.find('span', class_ = 'person-capacity').text.strip(' · ')
			room.review = s_div.find_all('span')[len(s_div.find_all('span')) - 1].text

			room_list.append(room)

	for room in room_list:
		print room.title
		print room.price
		print room.guests
		print room.review


	driver.quit()

	return room_list

	

get_all_room_all_page()