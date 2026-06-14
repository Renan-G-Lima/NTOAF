from src.team_repository import TeamRepository


teams = TeamRepository.get_all()

for team in teams:
    print(
        f"{team.id} | {team.name} | {team.abbreviation}"
    )