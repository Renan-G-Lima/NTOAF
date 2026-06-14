from sqlalchemy import select

from src.database import SessionLocal
from src.models import Team


class TeamRepository:

    @staticmethod
    def create(name: str, abbreviation: str) -> Team:
        with SessionLocal() as session:
            team = Team(
                name=name,
                abbreviation=abbreviation,
            )

            session.add(team)
            session.commit()
            session.refresh(team)

            return team

    @staticmethod
    def get_all() -> list[Team]:
        with SessionLocal() as session:
            result = session.scalars(
                select(Team).order_by(Team.name)
            )

            return list(result)
        
    @staticmethod
    def exists_by_abbreviation(abbreviation: str) -> bool:
        with SessionLocal() as session:
            team = session.scalar(
                select(Team).where(
                    Team.abbreviation == abbreviation
                )
            )

            return team is not None
        
    @staticmethod
    def update_elo(team_id: int, new_elo: int) -> None:
        with SessionLocal() as session:
            team = session.get(Team, team_id)

            if team is None:
                raise ValueError(f"Time {team_id} não encontrado")

            team.elo = new_elo

            session.commit()

    @staticmethod
    def get_by_id(team_id: int) -> Team | None:
        with SessionLocal() as session:
            return session.get(Team, team_id)

    @staticmethod
    def get_by_abbreviation(
        abbreviation: str,
    ) -> Team | None:

        with SessionLocal() as session:

            return session.scalar(
                select(Team).where(
                    Team.abbreviation == abbreviation
                )
            )
        
    @staticmethod
    def get_by_espn_id(
        espn_id: str,
    ) -> Team | None:

        with SessionLocal() as session:

            return session.scalar(
                select(Team).where(
                    Team.espn_id == espn_id
                )
            )
    
    @staticmethod
    def update_espn_id(
        team_id: int,
        espn_id: str,
    ) -> None:

        with SessionLocal() as session:

            team = session.get(
                Team,
                team_id
            )

            if team is None:
                raise ValueError(
                    f"Time {team_id} não encontrado"
                )

            team.espn_id = espn_id

            session.commit()

    @staticmethod
    def update_elo(
        team_id: int,
        new_elo: float,
    ) -> None:

        with SessionLocal() as session:

            team = session.get(
                Team,
                team_id,
            )

            if team is None:
                return

            team.elo = new_elo

            session.commit()

    @staticmethod
    def get_by_espn_id(
        espn_id: str,
    ):

        with SessionLocal() as session:

            return session.scalar(
                select(Team).where(
                    Team.espn_id == espn_id
                )
            )
        