from src.database import SessionLocal
from src.models import Game


class GameRepository:

    @staticmethod
    def create(
        home_team_id: int,
        away_team_id: int,
        home_score: int,
        away_score: int,
        season: int,
        week: int,
    ) -> Game:

        with SessionLocal() as session:

            game = Game(
                home_team_id=home_team_id,
                away_team_id=away_team_id,
                home_score=home_score,
                away_score=away_score,
                season=season,
                week=week,
            )

            session.add(game)
            session.commit()
            session.refresh(game)

            return game