# Take the code from the How To Decode A Website exercise (if you didnt do it or 
# just want to play with some different code, use the code from the solution), 
# and instead of printing the results to a screen, write the results to a txt
# file. In your code, just make up a name for the file you are saving to.
# 
# Extras:
# 
# Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup

base_url = 'https://kathmandupost.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features='html.parser')

filename = 'nytimes'
# filename = input("Enter filename to be saved: ") # extra
with open(filename, 'w') as f:
    for story_heading in soup.find_all('h3'):
        f.write(story_heading.text.replace('\n', ' ').strip())


