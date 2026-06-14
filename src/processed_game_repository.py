from sqlalchemy import select

from src.database import SessionLocal
from src.models import ProcessedGame


class ProcessedGameRepository:

    @staticmethod
    def exists(
        espn_event_id: str,
    ) -> bool:

        with SessionLocal() as session:

            game = session.scalar(
                select(ProcessedGame).where(
                    ProcessedGame.espn_event_id
                    == espn_event_id
                )
            )

            return game is not None

    @staticmethod
    def create(
        espn_event_id: str,
    ) -> None:

        with SessionLocal() as session:

            game = ProcessedGame(
                espn_event_id=espn_event_id
            )

            session.add(game)
            session.commit()