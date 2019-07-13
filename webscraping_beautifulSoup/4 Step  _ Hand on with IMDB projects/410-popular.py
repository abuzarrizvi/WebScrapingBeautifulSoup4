from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

class movies():
	"""docstring for Film"""
	def __init__(self):
		self.rank = ""
		self.title = ""		
		self.year = ""
		self.link="https://www.imdb.com"



def getfilmlist():
	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')


	url = 'https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm'

	driver.get(url)

	# print (driver.page_source)
	film_list = []
	soup = BeautifulSoup(driver.page_source,'lxml')

	table = soup.find('table', class_ = 'chart full-width')

	for td in table.find_all('td', class_ = 'titleColumn'):
		film=movies()

		a_tag = td.find('a')
		film.link += a_tag['href']
		fullname = td.text.strip().replace('\n','').replace('      ','')
		film.title = fullname
		print (fullname)		
		film_list.append(film)
	driver.quit()
	return film_list


def getposter(film_list):
	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
	if not os.path.exists('PopularFilmPosters'):
		os.makedirs('PopularFilmPosters')
	for film in film_list:
		url=film.link
		#url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
		driver.get(url)
		soup = BeautifulSoup(driver.page_source,'lxml')
		posterdiv = soup.find('div', class_='poster')
		posterhref = posterdiv.find('a')
		if posterhref is not None:
			posterlink = "https://www.imdb.com" + posterhref['href']

			driver.get(posterlink)
			soup = BeautifulSoup(driver.page_source,'lxml')
			divposter = soup.findAll('div',class_ = 'pswp__zoom-wrap')
			allimg = divposter[1].findAll('img')
			f = open('PopularFilmPosters\{0}.jpg'.format(film.title.replace(':','')), 'wb')
			f.write(requests.get(allimg[1]['src']).content)

			f.close()
	driver.quit()	

film_list=getfilmlist()

getposter(film_list[90:100])


	

