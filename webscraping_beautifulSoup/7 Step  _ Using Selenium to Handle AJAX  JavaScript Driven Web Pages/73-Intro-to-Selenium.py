from selenium import webdriver      # imports
from time import sleep
from bs4 import BeautifulSoup


# make a webdriver object   -    chrome driver path for my system -- >    /Users/waqarjoyia/Downloads/chromedriver


driver = webdriver.Chrome('/Users/waqarjoyia/Downloads/chromedriver')

# open some page using get method       - url -- > parameters

driver.get('https://www.facebook.com')

# driver.page_source

soup = BeautifulSoup(driver.page_source,'lxml')

print(soup.prettify())



# close webdriver object

driver.close()

