from src.betting_strategy import (
    is_bet_recommended
)
from src.prediction_repository import (
    PredictionRepository
)
from src.team_repository import (
    TeamRepository
)


predictions = PredictionRepository.get_all()

recommended = []

for prediction in predictions:

    if not is_bet_recommended(
        prediction.probability
    ):
        continue

    winner = TeamRepository.get_by_id(
        prediction.predicted_winner_id
    )

    recommended.append(
        (
            winner.name,
            prediction.probability
        )
    )

recommended.sort(
    key=lambda item: item[1],
    reverse=True
)

print()
print("=== RECOMMENDED BETS ===")
print()

for team_name, probability in recommended:

    print(
        f"{team_name}: "
        f"{probability:.2%}"
    )

print()
print(
    f"Total: {len(recommended)}"
)