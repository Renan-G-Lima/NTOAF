from src.prediction_service import (
    PredictionService
)
from src.upcoming_game_repository import (
    UpcomingGameRepository
)

from src.prediction_repository import (
    PredictionRepository
)

games = UpcomingGameRepository.get_all()

generated = 0

for game in games:

    if PredictionRepository.exists(
    home_team_id=game.home_team_id,
    away_team_id=game.away_team_id,
    season=game.season,
    week=game.week,
    ):
        print(
            f"Previsão já existe: "
            f"{game.id}"
        )
        continue

    PredictionService.predict_game(
        home_team_id=game.home_team_id,
        away_team_id=game.away_team_id,
        season=game.season,
        week=game.week,
    )

    generated += 1

print(
    f"Previsões geradas: {generated}"
)