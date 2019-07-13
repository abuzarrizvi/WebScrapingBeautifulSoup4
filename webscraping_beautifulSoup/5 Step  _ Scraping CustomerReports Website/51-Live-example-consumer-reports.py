from bs4 import BeautifulSoup
import re


def read_file():
    file = open('043consumer-reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

all_divs = soup.find_all('div',attrs={'class':'entry-letter'})

#print(all_divs)

products = [div.div.a.span.string for div in all_divs]

for product in products:
    print(product)