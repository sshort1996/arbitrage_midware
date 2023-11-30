from datetime import datetime
from utilities.Bet import Bet
from utilities.SportsBetAU import SportsBetAU


new_bet = Bet.create(
    event_id=1,
    bookmaker_id=1,
    sport="duck duck goose",
    event_date=datetime.strptime("2021-06-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
    event_tz="Australia/Perth",
    participants={"Silly Goose", "Daffy Duck"},
    outcome="win",
    target="Silly Goose",
    stake=99.0,
    odds=1.4,
    odds_unit="decimal",
)
print(new_bet)

sports_bet_AU = SportsBetAU()  # Create an instance of a specific bookmaker

# Place the bet with the chosen bookmaker
new_bet.place_with_bookmaker(sports_bet_AU)
