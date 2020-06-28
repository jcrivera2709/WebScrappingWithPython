import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get('https://forecast.weather.gov/MapClick.php?lat=26.71440000000007&lon=-80.05328999999995')
soup = BeautifulSoup(url.content, 'html.parser')
week_info = soup.find(id='seven-day-forecast')

# print(week_info)

items = week_info.find_all(class_='tombstone-container')
# print(items[0])

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())
print()

# List comprehension
# Loops through and finds all class names and puts them in a list
period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]

print(period_names)
print(short_desc)
print(temp)
print()

# Gets the info from the previous list comprehension
weather_info = pd.DataFrame({
    'period': period_names,
    'Short Description': short_desc,
    'Temperature': temp,
})

# Panda allows you to take the information and make it into a csv file.
weather_info.to_csv('weather.csv')

print(weather_info)
