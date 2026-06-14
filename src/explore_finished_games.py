import json
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

for event in data["events"]:

    status = event["status"]["type"]

    print(
        event["name"],
        "-",
        status["name"],
        "-",
        status["completed"]
    )

    if status["completed"]:

        print("\n=== JSON ===\n")

        print(
            json.dumps(
                event,
                indent=4
            )[:10000]
        )

        break

for competitor in (
    event["competitions"][0]["competitors"]
):

    print("\n---")

    print(
        "Team:",
        competitor["team"]["abbreviation"]
    )

    print(
        "Winner:",
        competitor["winner"]
    )

    print(
        "Score:",
        competitor["score"]
    )