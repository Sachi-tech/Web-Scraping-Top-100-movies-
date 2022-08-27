from bs4 import BeautifulSoup
import requests
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2"
response = requests.get(url)
response.raise_for_status()
html_website = response.text

soup = BeautifulSoup(html_website, "html.parse")


all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", "w") as movies_name:
    for movie in movies:
        movies_name.write(f'{movie} \n')
