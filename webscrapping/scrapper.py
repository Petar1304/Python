from bs4 import BeautifulSoup
import requests

data = requests.get('https://umggaming.com/leaderboards')
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(data.text, 'html.parser')

leaderboard = soup.find('table', {'id': 'leaderboard-table'})
tbody = leaderboard.find('tbody')

for tr in tbody.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    username = tr.find_all('td')[1].find_all('a')[1].text.strip()
    xp = tr.find_all('td')[3].text.strip()
    print(place, username, xp)
