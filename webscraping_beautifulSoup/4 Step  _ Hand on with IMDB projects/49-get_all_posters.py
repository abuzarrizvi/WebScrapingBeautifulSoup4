from bs4 import BeautifulSoup
from selenium import webdriver
import os
import requests

class posterpages():
	"""docstring for Film"""
	def __init__(self):
		self.link="https://www.imdb.com"



def getfilmlist():
	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')

	posterspages = []
	url = 'https://www.imdb.com/gallery/rg1624939264?ref_=nv_ph_lp'

	driver.get(url)

	# print (driver.page_source)
	film_list = []
	soup = BeautifulSoup(driver.page_source,'lxml')

	Right = soup.find_all('div',  {"id": "right"})
	spans = Right[0].find_all('span')
	page=posterpages()
	page.link='https://www.imdb.com/gallery/rg1624939264?ref_=nv_ph_lp'
	posterspages.append(page)
	for span in spans:
		herfs = span.find_all('a')
		for herf in herfs:
			page=posterpages()
			page.link+=herf['href']
			posterspages.append(page)
	driver.quit()
	return posterspages


def getposter(posters):
	driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')
	if not os.path.exists('Posters'):
		os.makedirs('Posters')
	for poster in posters:
		url=poster.link
		#url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
		driver.get(url)
		soup = BeautifulSoup(driver.page_source,'lxml')
		posterdiv = soup.find('div', class_='media_index_thumb_list')
		posterhrefs = posterdiv.find_all('a')
		for posterhref in posterhrefs:
			posterlink = "https://www.imdb.com" + posterhref['href']
			driver.get(posterlink)
			soup = BeautifulSoup(driver.page_source,'lxml')
			divposter = soup.findAll('div',class_ = 'pswp__zoom-wrap')
			allimg = divposter[1].findAll('img')

			div = soup.find('div', class_ = 'mediaviewer__footer')
			p = div.find('p')
			jpg_title = p.text
			jpg_title = jpg_title.replace(':','')
			
			jpg_title = jpg_title.replace('ë','')
			print(jpg_title)
			f = open('Posters\{0}.jpg'.format(jpg_title[0:20]), 'wb')
			f.write(requests.get(allimg[1]['src']).content)

			f.close()
	driver.quit()	

posters=getfilmlist()
for poster in posters:
	print (poster.link)
getposter(posters)


#getposter(film_list)



