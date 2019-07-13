from bs4 import BeautifulSoup


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# example  -- direct

# only returns first instance of 'p' tag
p = soup.p

print(p)



