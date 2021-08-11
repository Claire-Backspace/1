from typing import Text
import requests
from bs4 import BeautifulSoup

r = requests.get('https://roboppn.top/docs/README')
source = r.content
soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())
#print(soup.find('div'))
soup_new = soup.find('div', id = ("__docusaurus"))

for chapters in  soup_new.find_all('a'):

         print(chapters.text)
         #print(f"https://{chapters.attrs['href']}")
         print(chapters.attrs['href'])
