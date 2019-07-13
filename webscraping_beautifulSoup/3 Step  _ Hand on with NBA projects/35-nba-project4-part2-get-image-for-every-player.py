from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests
import time

class Player():
	"""docstring for Player"""
	def __init__(self):
		self.name = ""
		self.link = ""
		self.Height = ""
		self.Weight = ""
		self.Born = ""
		
		

def get_player_list():
	# create driver
	#driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
	#url = 'http://stats.nba.com/players/?ls=iref:nba:gnav'

	url = 'https://stats.nba.com/players/list/'
	# download html page
	driver.get(url)

	# print (driver.page_source)

	# create soup
	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', class_= 'stats-player-list players-list')   #'col-lg-12'

	# print (div)

	player_list = []


	for a in div.find_all('a'):
		# print (a.text)
		# print (a['href'])
		new_play = Player()
		new_play.name = a.text
		new_play.link = "https://stats.nba.com"+a['href']
		if new_play.name =="Run It":
			pass
		else:
			player_list.append(new_play)


	for one_player in player_list:

		print (one_player.name)
		print (one_player.link)

	driver.quit()

	return player_list


def get_detail_for_all_players(player_list):

	#driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
	for p in player_list[0:6]:

		# url = 'http://www.nba.com/playerfile/tony_allen/'
		
		url = p.link

		driver.get(url)

		# print (driver.page_source)

		soup = BeautifulSoup(driver.page_source, 'lxml')

		Height = ""
		Weight = ""
		Born = ""
		divspan = soup.find_all('div', class_ = 'player-stats__stat-title')
		for divs in divspan:
			if divs.text =="HT":
				for span in divs.findNextSiblings():
					Height = Height + span.text
					#print ("span height text")
					#print (span.text)
					#print ("div height text")
					#print (divs.text)
			elif divs.text =="WT":
				for span in divs.findNextSiblings():
					Weight = Weight + span.text
					#print ("span weight text")
					#print (span.text)
					#print ("div weight text")
					#print (divs.text)
			elif divs.text =="BORN":
				for span in divs.findNextSiblings():
					Born = Born + span.text
					#print ("span Born text")
					#print (span.text)
					#print ("div text")
					#print (divs.text)
		#player-stats__item player-stats__birthdate n-p columns small-3 medium-6
		#birthday = soup.find_all('div', class_ = 'player-stats__stat-title')
		#print (birthday.findNextSiblings())

		#birthdayspan = birthday.find('span', class_='player-stats__stat-value').text

		p.Height = Height
		p.Weight = Weight
		p.Born = Born #Born
		

	driver.quit()

	return player_list
	



#player_list=get_player_list()

#player_list = get_detail_for_all_players(player_list)

def get_nba_player_image(player_list):
	
	#driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
	if not os.path.exists('nba_player'):
		os.makedirs('nba_player')

	for player in player_list[0:4]:

		# url = 'http://www.nba.com/playerfile/tony_allen/'

		url = player.link

		driver.get(url)

		time.sleep(2)

		soup = BeautifulSoup(driver.page_source, 'lxml')

		# print (driver.page_source)

		div = soup.find('div', class_ = 'player-summary__image-block')

		img = div.find('img')

		print (img['src'])

		f = open('nba_player\{0}.jpg'.format(player.name),'wb')

		f.write(requests.get(img['src']).content)

		f.close()

	driver.quit()


get_nba_player_image( get_player_list() )


















"""docstring for Player"""

"""class Player():
	def __init__(self):
		self.name = ""
		self.link = ""
		self.Height = ""
		self.Weight = ""
		self.Born = ""
		
		

def get_player_list():
	# create driver
	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	url = 'http://stats.nba.com/players/?ls=iref:nba:gnav'

	# download html page
	driver.get(url)

	# print (driver.page_source)

	# create soup
	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', class_= 'col-lg-12')

	# print (div)

	player_list = []


	for a in div.find_all('a'):
		# print (a.text)
		# print (a['href'])
		new_play = Player()
		new_play.name = a.text
		new_play.link = a['href']
		player_list.append(new_play)


	for one_player in player_list:

		print (one_player.name)
		print (one_player.link)

	driver.quit()

	return player_list


def get_detail_for_all_players(player_list):

	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	for p in player_list[0:2]:

		# url = 'http://www.nba.com/playerfile/tony_allen/'

		url = p.link

		driver.get(url)

		# print (driver.page_source)

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

		# print (Height)
		# print (Weight)
		# print (Born)

		p.Height = Height
		p.Weight = Weight
		p.Born = Born

	driver.quit()

	return player_list
	

def get_nba_player_image(player_list):
	
	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	if not os.path.exists('nba_player'):
		os.makedirs('nba_player')

	for player in player_list:

		# url = 'http://www.nba.com/playerfile/tony_allen/'

		url = player.link

		driver.get(url)

		time.sleep(2)

		soup = BeautifulSoup(driver.page_source, 'lxml')

		# print (driver.page_source)

		div = soup.find('div', class_ = 'player-headshot')

		img = div.find('img')

		print (img['src'])

		f = open('nba_player\{0}.jpg'.format(player.name),'wb')

		f.write(requests.get(img['src']).content)

		f.close()

	driver.quit()


get_nba_player_image( get_player_list() )"""
