from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

body = soup.body

# contents - html -- we have already discussed about .contents function

#print(soup.html.contents)

# .previous_sibling -- returns previous sibling if exists otherwise return new line character

print(body.previous_sibling.previous_sibling)