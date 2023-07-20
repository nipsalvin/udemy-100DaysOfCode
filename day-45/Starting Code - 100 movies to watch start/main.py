import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')

all_movies = soup.find_all(name='h3', class_='title')

## Method 1 of creating a list
# descending_movies = []
# for title in all_movies:
#     movie = title.get_text()
#     descending_movies.append(movie)

## Method 2 of creating a list
descending_movies = [movie.get_text() for movie in all_movies]

# Method 1 of reversing list
# ascending_movies = list(reversed(descending_movies))

# Method 2 of reversing list
ascending_movies = descending_movies[::-1]

for movie in ascending_movies:
    with open('movies.txt', mode='a', encoding='utf-8') as data_file:
                    data_file.write(f'{movie} \n')
                    print(f'{movie} added to list')



