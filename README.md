# goalie-checker 🏒🥅

CLI for checking tonight's starting goalies in the NHL.

## How It Works?

The program simply fetches <a href="https://www.dailyfaceoff.com/starting-goalies/">https://www.dailyfaceoff.com/starting-goalies/</a>, parses the contents using BeautifulSoup, and prints the starting goalies for each of tonight's games. Note that the goalie situation may be fluid even close to the game.

## Running the Program

Requires Python 3. Install the required packages, e.g., with
```
pip3 install -r requirements.txt
```
Run the program with
```
python3 goalie.py
```

Note that the bindings to `python` and `pip` may vary depending on your system.

## Example Output

(Everything is `Uncofirmed`, as the league is in COVID19 lockdown while writing this).
```
NHL Starting Goalies: Sunday, March 22

Washington Capitals at Pittsburgh Penguins
Braden Holtby: Unconfirmed
Matt Murray: Unconfirmed

New York Rangers at Buffalo Sabres
Alexandar Georgiev: Unconfirmed
Linus Ullmark: Unconfirmed

Carolina Hurricanes at New York Islanders
Petr Mrazek: Unconfirmed
Semyon Varlamov: Unconfirmed

Winnipeg Jets at Dallas Stars
Connor Hellebuyck: Unconfirmed
Ben Bishop: Unconfirmed

Nashville Predators at Chicago Blackhawks
Juuse Saros: Unconfirmed
Corey Crawford: Unconfirmed

Arizona Coyotes at Los Angeles Kings
Darcy Kuemper: Unconfirmed
Jonathan Quick: Unconfirmed
```

## Something Broken?

As this program is a simple web scraper, changes to the source site (https://www.dailyfaceoff.com/starting-goalies/) may break it. Please report of any issues, or submit a PR!