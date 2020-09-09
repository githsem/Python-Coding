import requests

from bs4 import BeautifulSoup

url = "https://www.doviz.com/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

isim = soup.find_all("span",{"class":"name"})
kur =soup.find_all("span",{"class":"value"})


for i,j in zip(isim,kur):
    i = i.text
    j = j.text
    if i = "EURO":
        print(j)