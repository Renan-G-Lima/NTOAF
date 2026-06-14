import requests

from src.elo import update_elo
from src.team_repository import TeamRepository

URL = (
    "https://site.api.espn.com/apis/site/v2/"
    "sports/football/nfl/scoreboard"
    "?dates=20250105"
)

response = requests.get(
    URL,
    timeout=30,
)

event = response.json()["events"][0]

winner_team = None
loser_team = None

for competitor in (
    event["competitions"][0]["competitors"]
):

    espn_id = competitor["team"]["id"]

    team = TeamRepository.get_by_espn_id(
        espn_id
    )

    if competitor["winner"]:
        winner_team = team
    else:
        loser_team = team

print(
    f"Winner: {winner_team.name}"
)

print(
    f"Loser: {loser_team.name}"
)

print(
    f"Before -> "
    f"{winner_team.elo} / "
    f"{loser_team.elo}"
)

new_winner_elo, new_loser_elo = (
    update_elo(
        winner_team.elo,
        loser_team.elo,
    )
)

print(
    f"After -> "
    f"{new_winner_elo} / "
    f"{new_loser_elo}"
)