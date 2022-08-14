from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, "html.parser")

#print(soup.prettify())

title = soup.find('title')
copyright = soup.find("h6", class_="copyright")

print(title.string)
print(copyright.string)