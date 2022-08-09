import requests
from bs4 import BeautifulSoup

# url for the most popular movies on imdb
url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

r = requests.get(url)
c = r.content

soup = BeautifulSoup(c, "html.parser")

# scraping for movie poster
posters = []
all = soup.find_all("td", {"class": "posterColumn"})
for item in all:
    poster = item.find("img")
    posters.append(poster.get("src"))

# scraping for movie title
titles = []
all = soup.find_all("td", {"class": "titleColumn"})
for item in all:
    title = item.find("a").text
    titles.append(title)

# testing
print(posters)