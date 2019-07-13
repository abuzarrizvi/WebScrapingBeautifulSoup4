from selenium import webdriver
from bs4 import BeautifulSoup

class Player():
	"""docstring for Player"""
	def __init__(self):
		self.name = ""
		self.link = "https://stats.nba.com"
		
		

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

	div = soup.find('div', class_= 'stats-player-list players-list') # class_= 'col-lg-12'

	# print (div)

	player_list = []


	for a in div.find_all('a'):
		# print (a.text)
		# print (a['href'])
		new_play = Player()
		new_play.name = a.text
		new_play.link += a['href']
		player_list.append(new_play)


	for one_player in player_list:

		print (one_player.name)
		print (one_player.link)

	driver.quit()

	return player_list


get_player_list()