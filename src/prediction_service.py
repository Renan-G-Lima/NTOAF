from src.predictor import win_probability
from src.prediction_repository import PredictionRepository
from src.team_repository import TeamRepository


class PredictionService:

    @staticmethod
    def predict_game(
        home_team_id: int,
        away_team_id: int,
        season: int,
        week: int,
    ):

        home_team = TeamRepository.get_by_id(
            home_team_id
        )

        away_team = TeamRepository.get_by_id(
            away_team_id
        )

        if home_team is None:
            raise ValueError(
                f"Time {home_team_id} não encontrado"
            )

        if away_team is None:
            raise ValueError(
                f"Time {away_team_id} não encontrado"
            )

        home_probability = win_probability(
            team_elo=home_team.elo,
            opponent_elo=away_team.elo,
            is_home_team=True,
        )

        if home_probability >= 0.5:
            predicted_winner = home_team
            probability = home_probability
        else:
            predicted_winner = away_team
            probability = 1 - home_probability

        return PredictionRepository.create(
            home_team_id=home_team.id,
            away_team_id=away_team.id,
            predicted_winner_id=predicted_winner.id,
            probability=probability,
            season=season,
            week=week,
        )