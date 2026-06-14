import requests

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

event = data["events"][0]

print(
    "Event ID:",
    event["id"]
)

for competitor in (
    event["competitions"][0]["competitors"]
):

    print(
        competitor["team"]["abbreviation"],
        "| Winner:",
        competitor["winner"],
        "| ESPN ID:",
        competitor["team"]["id"]
    )