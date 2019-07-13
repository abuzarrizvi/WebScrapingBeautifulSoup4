from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

p = (soup.body.p)


# .next_siblings

for sibling in p.next_siblings:
    #print(sibling.name if sibling != '\n' else '')
    pass


# .previous_siblings

for sibling in p.previous_siblings:
    print(sibling if sibling  != '\n' else '')
