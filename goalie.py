from bs4 import BeautifulSoup
from urllib import request

url = "https://www.dailyfaceoff.com/starting-goalies"

req = request.Request(url, headers={"User-Agent": "Not a bot ;)"})
try:
    page = request.urlopen(req)
except Exception as e:
    print(e)

soup = BeautifulSoup(page, "html.parser")

main_heading = soup.find("h1").text.strip()


print(main_heading)
print()
games = soup.find_all("article")
for game in games:
    game_heading = game.div.span.text.strip()
    print(game_heading)
    goalies = game.select("& > div:nth-of-type(2) > div > div > div:nth-of-type(2)")
    for goalie in goalies:
        goalie_name = goalie.div.span.text.strip()
        goalie_strength = (
            goalie.select("& > div:nth-of-type(2) > div > span:last-of-type")[0]
            .get_text()
            .strip()
        )
        print("%s: %s" % (goalie_name, goalie_strength))
