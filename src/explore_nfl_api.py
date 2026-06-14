import json
import requests


url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"

response = requests.get(
    url,
    timeout=30,
)

data = response.json()

first_team = (
    data["sports"][0]
    ["leagues"][0]
    ["teams"][0]
)

print(
    json.dumps(
        first_team,
        indent=4
    )
)