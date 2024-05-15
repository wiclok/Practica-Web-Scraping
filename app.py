import requests

def Web_Crawling(url):
  response = requests.get(url)

def Execute_Program():
  url = 'https://books.toscrape.com/'
  Web_Crawling(url)

if __name__ == '__main__':
  Execute_Program()