import requests
from bs4 import BeautifulSoup

def Web_Crawling(url):
  response = requests.get(url)
  return response

def Execute_Program():
  url = 'https://books.toscrape.com/'
  web_crawling = Web_Crawling(url)
  

if __name__ == '__main__':
  Execute_Program()