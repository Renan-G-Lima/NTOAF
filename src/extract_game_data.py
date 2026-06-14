import requests


url = (
    "https://site.api.espn.com/apis/site/v2/"
    "sports/football/nfl/scoreboard"
)

response = requests.get(
    url,
    timeout=30,
)

data = response.json()

event = data["events"][0]

competition = event["competitions"][0]

for competitor in competition["competitors"]:

    print("-----")

    print(
        "HOME/AWAY:",
        competitor["homeAway"]
    )

    print(
        "TEAM ID:",
        competitor["team"]["id"]
    )

    print(
        "TEAM:",
        competitor["team"]["displayName"]
    )

    print(
        "ABBREVIATION:",
        competitor["team"]["abbreviation"]
    )