from src.team_repository import (
    TeamRepository
)

team = TeamRepository.get_by_espn_id(
    "12"
)

print(team.name)
print(team.abbreviation)
print(team.elo)