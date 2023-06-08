import requests
from bs4 import BeautifulSoup




url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

movies = soup.select('td.titleColumn')
ratings = soup.select('td.imdbRating strong')

for index, movie in enumerate(movies):
    title = movie.find('a').text
    year = movie.find('span').text
    rating = ratings[index].text.strip()

    print(f"{title} ({year}) - Rating: {rating}")


import csv

# Assuming you have extracted a list of dictionaries where each dictionary represents an item
data = [
    {'title':'Article 1', 'description' : 'Description 1'},
    {'title':'Article 2', 'description' : 'Description 2'},
]
filename = 'scraped_data.csv'
fieldnames = ['title', 'description']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
