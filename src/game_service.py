from src.elo import calculate_new_elo
from src.game_repository import GameRepository
from src.team_repository import TeamRepository


class GameService:

    @staticmethod
    def register_game(
        home_team_id: int,
        away_team_id: int,
        home_score: int,
        away_score: int,
        season: int,
        week: int,
    ):

        teams = TeamRepository.get_all()

        home_team = next(
            team for team in teams
            if team.id == home_team_id
        )

        away_team = next(
            team for team in teams
            if team.id == away_team_id
        )

        GameRepository.create(
            home_team_id=home_team_id,
            away_team_id=away_team_id,
            home_score=home_score,
            away_score=away_score,
            season=season,
            week=week,
        )

        if home_score > away_score:
            home_result = 1
            away_result = 0
        else:
            home_result = 0
            away_result = 1

        new_home_elo = calculate_new_elo(
            team_elo=home_team.elo,
            opponent_elo=away_team.elo,
            result=home_result,
        )

        new_away_elo = calculate_new_elo(
            team_elo=away_team.elo,
            opponent_elo=home_team.elo,
            result=away_result,
        )

        TeamRepository.update_elo(
            team_id=home_team.id,
            new_elo=new_home_elo,
        )

        TeamRepository.update_elo(
            team_id=away_team.id,
            new_elo=new_away_elo,
        )