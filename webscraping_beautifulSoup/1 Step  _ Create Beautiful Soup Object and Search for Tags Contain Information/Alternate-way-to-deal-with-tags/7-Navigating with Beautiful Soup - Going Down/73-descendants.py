from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# .contents             --- returns us direct children of the said tag

body = soup.body

children = [child for child in body.contents if child != '\n'] # alternate way to populate the list called list comprehension
#print(children)

#print(len(children))



# .descendants  -- returns us all the children of the said tag -- generator


for index,child in enumerate(soup.head.descendants):
    print(index)
    print(child if child != '\n' else '\\n')

