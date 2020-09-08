import requests

from bs4 import BeautifulSoup

url = "https://www.n11.com/"
response = requests.get(url)
html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

for i in soup.find_all("a"):
    print(i.get("href"))