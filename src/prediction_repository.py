from sqlalchemy import select

from src.database import SessionLocal
from src.models import Prediction


class PredictionRepository:

    @staticmethod
    def create(
        home_team_id: int,
        away_team_id: int,
        predicted_winner_id: int,
        probability: float,
        season: int,
        week: int,
    ) -> Prediction:

        with SessionLocal() as session:

            prediction = Prediction(
                home_team_id=home_team_id,
                away_team_id=away_team_id,
                predicted_winner_id=predicted_winner_id,
                probability=probability,
                season=season,
                week=week,
            )

            session.add(prediction)
            session.commit()
            session.refresh(prediction)

            return prediction

    @staticmethod
    def get_all() -> list[Prediction]:
        with SessionLocal() as session:
            result = session.scalars(
                select(Prediction)
            )

            return list(result)
        
    @staticmethod
    def update_result(
        prediction_id: int,
        correct: bool,
    ) -> None:

        with SessionLocal() as session:

            prediction = session.get(
                Prediction,
                prediction_id
            )

            if prediction is None:
                raise ValueError(
                    f"Previsão {prediction_id} não encontrada"
                )

            prediction.correct = correct

            session.commit()

    @staticmethod
    def exists(
        home_team_id: int,
        away_team_id: int,
        season: int,
        week: int,
    ) -> bool:

        with SessionLocal() as session:

            prediction = session.scalar(
                select(Prediction).where(
                    Prediction.home_team_id == home_team_id,
                    Prediction.away_team_id == away_team_id,
                    Prediction.season == season,
                    Prediction.week == week,
                )
            )

            return prediction is not None