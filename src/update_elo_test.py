from src.elo import calculate_new_elo
from src.team_repository import TeamRepository


teams = TeamRepository.get_all()

chiefs = next(
    team for team in teams
    if team.abbreviation == "KC"
)

ravens = next(
    team for team in teams
    if team.abbreviation == "BAL"
)

new_elo = calculate_new_elo(
    team_elo=chiefs.elo,
    opponent_elo=ravens.elo,
    result=1,
)

TeamRepository.update_elo(
    team_id=chiefs.id,
    new_elo=new_elo,
)

print(
    f"{chiefs.name}: "
    f"{chiefs.elo} -> {new_elo}"
)