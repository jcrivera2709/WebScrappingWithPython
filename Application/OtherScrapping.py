import requests
from bs4 import BeautifulSoup
import pandas as pd

url2 = requests.get('http://quotes.toscrape.com/')
soup2 = BeautifulSoup(url2.content, 'html.parser')
quotes = soup2.find_all(class_='quote')

print(quotes[0].find(class_='text').get_text())

text = [item.find(class_='text').get_text() for item in quotes]
author = [item.find(class_='author').get_text() for item in quotes]

print(text)
print()

quote_and_author = pd.DataFrame({
    'Quote': text,
    'Author': author,
})

print(quote_and_author)
quote_and_author.to_csv('quotes.csv')
