from datetime import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_kinoafisha_films(year):
    data = []
    url = f'https://www.kinoafisha.info/rating/movies/{year}/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    entries = soup.find_all("div", class_="movieList_item movieItem movieItem-rating movieItem-position")
    for entry in entries:
            movieItem_info = entry.find("div",class_= "movieItem_info")
            film_name = movieItem_info.find("a",class_="movieItem_title").text

            movieItem_details = entry.find("div", class_="movieItem_details")
            release_date = movieItem_details.find("span", class_="movieItem_year").text.split(",")[0]

            country = movieItem_details.find("span", class_="movieItem_year").text.split(",")[1]
            genre = movieItem_details.find("span", class_="movieItem_genres").text
            rating = entry.find("span").text

            data.append({"film name": film_name,"release_date": release_date,"country": country,"genre": genre,"rating":rating})
    return data


year = 2025
if year > datetime.today().year:
    print(f"ЭТОТ ГОД ЕЩЁ НЕ НАСТУПИЛ )))")
    exit(1)

kinoafisha_films = collect_kinoafisha_films(year)
print(f"ТОП 10 ФИЛЬМОВ ЗА {year} год :")
for i,j in enumerate(kinoafisha_films[:10]):
    print(i+1,j)

print()
print(f"ТОП 10 ЖАНРОВ ФИЛЬМОВ ЗА {year} год :")
for i,j in enumerate(kinoafisha_films[:10]):
    print(i+1,j["genre"])

df = pd.DataFrame(kinoafisha_films[:10])
df.to_excel('kinoafisha_films.xlsx')