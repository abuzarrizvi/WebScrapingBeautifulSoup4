import requests
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
from selenium import webdriver

#user_agent = UserAgent()
main_url = 'http://codingbat.com/java'
#page = requests.get(main_url,headers={'user-agent':user_agent.chrome})
#soup = BeautifulSoup(page.content,'lxml')

driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')

driver.get(main_url)
soup = BeautifulSoup(driver.page_source,'lxml')

base_url = 'http://codingbat.com'

all_divs = soup.find_all('div',class_='summ')

all_links = [base_url + div.a['href'] for div in all_divs]


# part 2
print(all_links)
question_links=[]
for link in all_links:
    driver.get(link)
    inner_soup = BeautifulSoup(driver.page_source,'lxml')
    div = inner_soup.find('div',class_='tabc')
    question_links = [base_url + td.a['href'] for td in div.table.find_all('td')]


# part 3

    for question_link in question_links:
        driver.get(question_link)
        final_soup = BeautifulSoup(driver.page_source,'lxml')
        indent_div = final_soup.find('div', attrs={'class':'indent'})
        #print(indent_div.table)
        problem_statement = indent_div.table.div.text
       



        siblings_of_statement = indent_div.table.div.next_siblings

        examples = [sibling for sibling in siblings_of_statement if sibling.string is not None]

        print(problem_statement)
        for example in examples:
            print(example)
            pass
        print('\n\n\n')
driver.quit()