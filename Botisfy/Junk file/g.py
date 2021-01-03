import wikipedia
import unicodedata
a = wikipedia.search('game')

title = u'{a[0]}'
value = str(title)
print(value, type(value))

print(wikipedia.summary(f'{title}', sentences=1))




import wikipedia
import subprocess
from pprint import pprint
from bs4 import BeautifulSoup
import requests
key = 'dog'
source = requests.get(f'https://www.google.com/search?tbm=isch&q={key}')
#encodings = 'utf-8'
#html = source.decode(encodings)

#key = BeautifulSoup(source,"lxml")
#prettify
print(source.headers)
