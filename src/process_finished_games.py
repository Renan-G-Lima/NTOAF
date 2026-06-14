import requests

from src.elo import update_elo
from src.team_repository import TeamRepository
from src.processed_game_repository import (
    ProcessedGameRepository
)

URL = (
    "https://site.api.espn.com/apis/site/v2/"
    "sports/football/nfl/scoreboard"
    "?dates=20250105"
)

response = requests.get(
    URL,
    timeout=30,
)

data = response.json()

processed = 0

for event in data["events"]:

    event_id = event["id"]

    if ProcessedGameRepository.exists(
        event_id
    ):
        continue

    competitors = (
        event["competitions"][0]["competitors"]
    )

    winner_team = None
    loser_team = None

    for competitor in competitors:

        team = (
            TeamRepository.get_by_espn_id(
                competitor["team"]["id"]
            )
        )

        if competitor["winner"]:
            winner_team = team
        else:
            loser_team = team

    if (
        winner_team is None
        or loser_team is None
    ):
        continue

    new_winner_elo, new_loser_elo = (
        update_elo(
            winner_team.elo,
            loser_team.elo,
        )
    )

    TeamRepository.update_elo(
        winner_team.id,
        new_winner_elo,
    )

    TeamRepository.update_elo(
        loser_team.id,
        new_loser_elo,
    )

    ProcessedGameRepository.create(
        event_id
    )

    processed += 1

    print(
        f"Processed: "
        f"{winner_team.abbreviation} "
        f"beat "
        f"{loser_team.abbreviation}"
    )

print(
    f"\nTotal processed: {processed}"
)