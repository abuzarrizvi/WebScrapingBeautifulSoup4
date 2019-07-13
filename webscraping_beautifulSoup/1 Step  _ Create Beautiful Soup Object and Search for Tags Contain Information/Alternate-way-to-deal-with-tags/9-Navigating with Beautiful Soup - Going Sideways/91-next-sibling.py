from bs4 import BeautifulSoup



def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

body = soup.body
p = soup.body.p


# body - contents -- we have already discussed about .contents function


#print(body.contents)


# .next_sibling -- returns next sibling if exists otherwise return new line character


print(p.next_sibling.next_sibling)

