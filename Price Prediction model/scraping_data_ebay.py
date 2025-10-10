import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from itertools import zip_longest

df = pd.read_csv('links_ebay_no_duplicate.csv')

links = df['links']

title, price, etat, info = [], [], [], []

i=1
for link in links:
    page = requests.get(link)
    sp = BeautifulSoup(page.content,'lxml')

    lap_title = sp.find('h1',{'class':'x-item-title__mainTitle'})
    lap_price = sp.find('div',{'class':'x-price-primary'})
    lap_etat = sp.find('span',{'class':'ux-icon-text__text'})
    lap_info = sp.find('div',{'class':"ux-layout-section-evo ux-layout-section--features",'data-testid':"ux-layout-section-evo"})
            
      
    title.append(lap_title.text.strip() if lap_title else "not found")
    price.append(lap_price.text.strip() if lap_price else "not found")
    etat.append(lap_etat.text.strip() if lap_etat else "not found")
    info.append(lap_info.text.strip() if lap_info else "not found")

    print(f'link {i} was scraped')
    i = i + 1

header = ['title','current_price','etat','info']
data = [title, price, etat, info]
rows = zip_longest(*data)

#save data in csv file
with open('data_laptop_ebay_2.csv', 'w', newline='', encoding='UTF-8') as file:
    wr = csv.writer(file)
    wr.writerow(header)
    wr.writerows(rows)
