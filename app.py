import requests

url = 'https://books.toscrape.com/'

response = requests.get(url)

print(response.text)