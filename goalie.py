from bs4 import BeautifulSoup
from urllib import request

url = "https://www.dailyfaceoff.com/starting-goalies/"

req = request.Request(url, headers={"User-Agent": "Not a bot ;)"})
try:
    page = request.urlopen(req)
except Exception as e:
    print(e)

soup = BeautifulSoup(page, "html.parser")

main_heading = soup.find("h1", attrs={"class": "heading"}).text.strip()


print(main_heading)
print()
goalie_cards = soup.find_all("div", attrs={"class": "starting-goalies-card"})

for card in goalie_cards:
    game_heading = card.h4.text.strip()
    print(game_heading)

    away_goalie_name = card.select(".away-goalie .meta-row h4")[0].text.strip()
    away_goalie_strength = (
        card.select(".away-goalie .news-strength")[0].get_text().strip()
    )
    print("%s: %s" % (away_goalie_name, away_goalie_strength))

    home_goalie_name = card.select(".home-goalie .meta-row h4")[0].text.strip()
    home_goalie_strength = (
        card.select(".home-goalie .news-strength")[0].get_text().strip()
    )
    print("%s: %s" % (home_goalie_name, home_goalie_strength))
    print()
