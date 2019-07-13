from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

title = soup.title

parent = title.parent




# .parent -- returns only instance parent information

p = soup.p

print(p)
#print(p.parent.name)



# html

html = soup.html

#print(type(html.parent))         #   bs4 --- html ----


# soup

print(soup.parent)