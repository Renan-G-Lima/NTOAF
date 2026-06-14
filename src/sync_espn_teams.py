import requests

from src.team_repository import TeamRepository


URL = (
    "https://site.api.espn.com/apis/site/v2/"
    "sports/football/nfl/teams"
)


response = requests.get(
    URL,
    timeout=30,
)

data = response.json()

teams = (
    data["sports"][0]
    ["leagues"][0]
    ["teams"]
)

updated = 0

for item in teams:

    espn_team = item["team"]

    abbreviation = espn_team["abbreviation"]
    espn_id = espn_team["id"]

    team = TeamRepository.get_by_abbreviation(
        abbreviation
    )

    if team is None:
        print(
            f"❌ Não encontrado: {abbreviation}"
        )
        continue

    print(
        f"✅ Encontrado: {abbreviation}"
    )

    TeamRepository.update_espn_id(
        team.id,
        espn_id,
    )

    updated += 1

    print(
        f"{abbreviation} -> ESPN {espn_id}"
    )

print()
print(
    f"Times atualizados: {updated}"
)