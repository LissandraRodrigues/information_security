import json

from urllib.request import urlopen

url = 'https://ipinfo.io/json'

answer = urlopen(url)

data = json.load(answer)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print(f'''

Dados do seu IP Externo

IP: {ip}
País: {country}
Região: {region}
Cidade: {city}
Organização: {org}

''')


