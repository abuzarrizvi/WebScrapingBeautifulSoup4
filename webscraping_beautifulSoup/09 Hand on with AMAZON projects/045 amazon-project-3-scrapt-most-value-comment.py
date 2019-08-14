from bs4 import BeautifulSoup
from selenium import webdriver


class Book():
	def __init__(self):
		self.title = ""
		self.detail_link = ""


def get_python_book_list():
	
	book_list = []

	#driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
	url = 'https://www.amazon.com/s/ref=sr_pg_100?rh=n%3A283155%2Ck%3Apython+programming&page=1'
	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	# print soup.prettify()

	ul = soup.find('ul',{'id':'s-results-list-atf'})

	for a in ul.find_all('a', class_= 's-access-detail-page'):

		new_book = Book()
		new_book.title = a.text
		new_book.detail_link = a['href']
		book_list.append(new_book)

		print a.text
		print a['href']
		print '\n'

	return book_list


class Comment():
	def __init__(self):
		self.title = ""
		self.content = ""
		
		

def get_most_value_comment_for_product(url):
	
	comment_list = []

	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')	
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'lxml')

	# print soup.prettify()

	div = soup.find('div', {'id':'revMHRL'})

	for div1 in div.find_all('div',class_='a-section celwidget'):

		cm = Comment()
		cm.title = div1.find('span',class_='a-size-base a-text-bold').text
		cm.content = div1.find('div', class_='a-section').text

		comment_list.append(cm)
		

	for cm in comment_list:
		print cm.title
		print cm.content
		print '\n'

	return comment_list


url = 'https://www.amazon.com/Python-Programming-Introduction-Computer-Science/dp/1590282418'
get_most_value_comment_for_product(url)