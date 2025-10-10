import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from itertools import zip_longest

df = pd.read_csv('links_ebay_no_duplicate.csv')

links = df['links']

title, price, image, link = [], [], [], []

i=1
for j in links:
    page = requests.get(j)
    sp = BeautifulSoup(page.content,'lxml')

    lap_title = sp.find('h1',{'class':'x-item-title__mainTitle'})
    lap_price = sp.find('div',{'class':'x-price-primary'})
    image_div = sp.find("div",{'class':"ux-image-carousel-item"})
    image_tag = image_div.find("img") if image_div else None

    if image_tag: image.append(image_tag.get("src"))        
    title.append(lap_title.text.strip() if lap_title else "not found")
    price.append(lap_price.text.strip() if lap_price else "not found")
    link.append(j)

    print(f'{i} scraped')
    i = i + 1


header = ['title','current_price','etat','info','rating']
data = [title, price, link, image]
rows = zip_longest(*data)
with open('data_model_2.csv', 'w', newline='', encoding='UTF-8') as file:
    wr = csv.writer(file)
    wr.writerow(header)
    wr.writerows(rows)
