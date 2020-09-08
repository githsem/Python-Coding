import requests

from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=ankara"
response = requests.get(url)
