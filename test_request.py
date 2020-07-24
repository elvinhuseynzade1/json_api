import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

html_ici = response.content

soup = BeautifulSoup(html_ici,"html.parser")

a = float(input("Ratingi daxil edin:"))

basliqlar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class","ratingColumn imdbRating"})

for basliq, rating in zip(basliqlar,ratingler):
    basliq = basliq.text
    rating = rating.text

    basliq = basliq.strip()
    basliq = basliq.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) >= a):
        print("Film adi: {} Filmin ratingi : {}".format(basliq,rating))