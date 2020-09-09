import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

basliklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

a= float(input("Rating Giriniz :"))
for baslik,rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")
    baslik = baslik.strip("0123456789. ")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if float(rating)>a:
        print("Film Adi : ",baslik)
        print("Rating : ",rating)
        print("***********************************************************")
