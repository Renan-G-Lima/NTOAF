from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    abbreviation: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)

    elo: Mapped[int] = mapped_column(Integer, default=1500)

    espn_id: Mapped[str | None] = mapped_column(
    nullable=True,
    unique=True
    )

class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    home_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    away_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    home_score: Mapped[int] = mapped_column(Integer)
    away_score: Mapped[int] = mapped_column(Integer)

    season: Mapped[int] = mapped_column(Integer)
    week: Mapped[int] = mapped_column(Integer)

class UpcomingGame(Base):
    __tablename__ = "upcoming_games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    home_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    away_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    season: Mapped[int] = mapped_column(Integer)
    week: Mapped[int] = mapped_column(Integer)

    game_date: Mapped[str | None] = mapped_column(
    nullable=True
    )

class Prediction(Base):
    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    home_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    away_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    predicted_winner_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    probability: Mapped[float]

    season: Mapped[int] = mapped_column(Integer)
    week: Mapped[int] = mapped_column(Integer)

    correct: Mapped[bool | None] = mapped_column(
        nullable=True,
        default=None
    )

    sportsbook_odds: Mapped[float | None] = mapped_column(
        nullable=True,
        default=None
    )

class ProcessedGame(Base):
    __tablename__ = "processed_games"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    espn_event_id: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )