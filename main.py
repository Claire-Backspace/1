import requests
import re
from bs4 import BeautifulSoup
from requests.api import get
from requests.sessions import session
url = 'https://roboppn.top/'
# r = session.get(url)
# print(r.html.text)
strhtml = requests.get(url)
soupdata = BeautifulSoup(strhtml.text, 'html.parser')
data = soupdata.select('div.col--4 > div > a > h3')
# div.col--4:nth-child(1) > div:nth-child(2) > a:nth-child(1) > h3:nth-child(1)
for item in data:
   result={
     'title':item.get_text(),
     'link':item.get('href'),       
     'id': re.findall('\d+',str( item.get('href') ))
}
