import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import json

# url = "https://www.kinopoisk.ru/lists/movies/genre--horror/?sort=rating&b=films&page=1"
#
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 "
                  "YaBrowser/21.6.2.817 (beta) Yowser/2.5 Safari/537.36",
    "Accept": "*/*"
}
#
all_films = []
count = 0
#
for i in range(1, 5):
#     req = requests.get(f"https://www.kinopoisk.ru/lists/movies/genre--horror/?sort=rating&b=films&page={i}",
#                        headers=headers)
#     src = req.text
#
    # with open(f"data/index{i}.html", "w", encoding='utf-8') as file:
    #     file.write(src)

    with open(f"data/index{i}.html", encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    all_films_hrefs = soup.find_all(class_="styles_upper__j8BIs")

    for item in all_films_hrefs:
        item_text = item.find(class_="base-movie-main-info_link__YwtP1").find('span').text
        item_href = "https://www.kinopoisk.ru"+item.find(class_="base-movie-main-info_link__YwtP1").get("href")
        rating = item.find(class_="styles_kinopoiskValue__9qXjg")
        rating_films = rating.text
        year = item.find(class_="desktop-list-main-info_secondaryText__M_aus")
        year_films = year.text.split(",")
        if len(year_films) == 2:
            year_film = year_films[0]
        elif len(year_films) > 3:
            year_film = year_films[2]
        else:
            year_film = year_films[1]
        count += 1
        print(count)
        all_films_hrefs_dict = {
            "model": "MainApp.movies",
            "pk": count,
            "fields":
                {"title": item_text,
                 "year": int(year_film),
                 "film_ratings": float(rating_films),
                 "link": item_href
                 }
            }
        all_films.append(all_films_hrefs_dict)
    # sleep(random.randrange(5, 15))
#
with open("fixtures/all_movies_dict.json", "w", encoding='utf-8') as file:
    json.dump(all_films, file, indent=4, ensure_ascii=False)





