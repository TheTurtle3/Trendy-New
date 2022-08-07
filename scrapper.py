import requests
from bs4 import BeautifulSoup

# url for the most popular movies on imdb
url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

r = requests.get(url)

c = r.content

soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("tbody", {"class": "lister-list"})



print(all)