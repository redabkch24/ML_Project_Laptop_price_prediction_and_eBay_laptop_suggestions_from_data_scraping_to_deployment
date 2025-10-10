import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from itertools import zip_longest


links_list = []

for num_page in range(1,151):
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw=laptop&_sacat=0&_pgn={num_page}'
    page = requests.get(url)
    sp = BeautifulSoup(page.content, 'lxml')
    links = sp.find_all('a',{'_sp':"p2351460.m1686.l7400"})
    for link in links:
        tmp = link.get('href')
        if tmp:
            links_list.append(tmp)
    print(f'{num_page} was scraped')

df = pd.DataFrame(links_list, columns=['links'])
dff = df.drop_duplicates()
dff.to_csv('scraping_links_ebay.csv')
