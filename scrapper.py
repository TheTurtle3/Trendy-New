import requests
from bs4 import BeautifulSoup
import sqlite3


# creating a db 
con = sqlite3.connect("trendynew.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS movies(title text, poster text)''')
cur.execute('''CREATE TABLE IF NOT EXISTS shows(title text, poster text)''')


# clearing the tables before adding new data
cur.execute("DELETE FROM movies")
cur.execute("DELETE FROM shows")


# setting up scraper for most popular movies
url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm" # imdb url for most popular movies
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c, "html.parser")


# scraping for movie poster src (instead of going into the seperate div to get title of the movie as before,
# it is easier and more efficient to get the 'alt' attribute of the img as it is the title of the movie).
all = soup.find_all("td", {"class": "posterColumn"})
for item in all:
    img = item.find("img")
    imgsrc = img.get("src")
    title = img.get("alt")

    # adding the name and imgsrc to db
    cur.execute("INSERT INTO movies VALUES (?, ?)", (title, imgsrc))


# setting up scraper for most popular shows
url = "https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv" # imdb url to most popular shows
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c, "html.parser")

# scraping for show poster src and show title
all = soup.find_all("td", {"class": "posterColumn"})
for item in all:
    img = item.find("img")
    imgsrc = img.get("src")
    title = img.get("alt")
    
    # adding the name and imgsrc to db
    cur.execute("INSERT INTO shows VALUES (?, ?)", (title, imgsrc))


# commiting changes and closing the connection to database
con.commit()
con.close()