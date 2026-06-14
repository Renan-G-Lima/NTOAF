import requests

from src.team_repository import TeamRepository
from src.upcoming_game_repository import (
    UpcomingGameRepository,
)

URL = (
    "https://site.api.espn.com/apis/site/v2/"
    "sports/football/nfl/scoreboard"
)

response = requests.get(
    URL,
    timeout=30,
)

data = response.json()

events = data["events"]

imported = 0

for event in events:

    competition = event["competitions"][0]

    competitors = competition["competitors"]

    home = next(
        c for c in competitors
        if c["homeAway"] == "home"
    )

    away = next(
        c for c in competitors
        if c["homeAway"] == "away"
    )

    home_team = TeamRepository.get_by_espn_id(
        home["team"]["id"]
    )

    away_team = TeamRepository.get_by_espn_id(
        away["team"]["id"]
    )

    if home_team is None or away_team is None:
        print(
            f"Falha no mapeamento: "
            f"{event['name']}"
        )
        continue

    if UpcomingGameRepository.exists(
    home_team_id=home_team.id,
    away_team_id=away_team.id,
    season=event["season"]["year"],
    week=event["week"]["number"],
    ):
        print(
            f"Jogo já existe: "
            f"{event['name']}"
        )
        continue

    UpcomingGameRepository.create(
        home_team_id=home_team.id,
        away_team_id=away_team.id,
        season=event["season"]["year"],
        week=event["week"]["number"],
        game_date=event["date"],
    )

    imported += 1

    print(
        f"{away_team.name} @ "
        f"{home_team.name}"
    )

print()
print(
    f"Jogos importados: {imported}"
)