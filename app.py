import requests
from bs4 import BeautifulSoup

def Web_Crawling(url):
  response = requests.get(url)
  
  return response.text

def extract_all_tags_hyperlinks(web_crawler):
  soup = BeautifulSoup(web_crawler, 'html.parser')
  
  all_tags_hyperlinks = soup.find_all('a')
  
  return all_tags_hyperlinks

def Execute_Program():
  
  url = 'https://books.toscrape.com/'
  web_crawler = Web_Crawling(url)
  
  all_tag_hyperlink = extract_all_tags_hyperlinks(web_crawler)
  
  
  

if __name__ == '__main__':
  Execute_Program()