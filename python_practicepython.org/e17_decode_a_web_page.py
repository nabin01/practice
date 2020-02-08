# Use the BeautifulSoup and requests Python packages to print out a list of all
# the article titles on the Kathmandupost homepage.
# Kathmandupost is a Nepali web news portal. (kathmandupost.com)

import requests
from bs4 import BeautifulSoup

r = requests.get('https://kathmandupost.com')
soup = BeautifulSoup(r.text, features='html.parser')
print("Headlines today: ")
# h3 tag stores headlines in kathmandupost 
for c, i in enumerate(soup.find_all('h3'), 1):
    print(f'{c} = {i.text}')
