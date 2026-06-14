from sqlalchemy import select

from src.database import SessionLocal
from src.models import UpcomingGame


class UpcomingGameRepository:

    @staticmethod
    def create(
        home_team_id: int,
        away_team_id: int,
        season: int,
        week: int,
        game_date: str | None = None,
    ) -> UpcomingGame:

        with SessionLocal() as session:

            game = UpcomingGame(
                home_team_id=home_team_id,
                away_team_id=away_team_id,
                season=season,
                week=week,
                game_date=game_date,
            )

        session.add(game)
        session.commit()
        session.refresh(game)

        return game
    
    @staticmethod
    def exists(
        home_team_id: int,
        away_team_id: int,
        season: int,
        week: int,
    ) -> bool:

        with SessionLocal() as session:

            game = session.scalar(
                select(UpcomingGame).where(
                    UpcomingGame.home_team_id == home_team_id,
                    UpcomingGame.away_team_id == away_team_id,
                    UpcomingGame.season == season,
                    UpcomingGame.week == week,
                )
            )

        return game is not None

    @staticmethod
    def get_all() -> list[UpcomingGame]:

        with SessionLocal() as session:

            result = session.scalars(
                select(UpcomingGame)
            )

            return list(result)
        
    @staticmethod
    def get_all() -> list[UpcomingGame]:

        with SessionLocal() as session:

            result = session.scalars(
                select(UpcomingGame)
            )

            return list(result)