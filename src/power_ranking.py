from src.team_repository import TeamRepository


def get_power_ranking():
    teams = TeamRepository.get_all()

    return sorted(
        teams,
        key=lambda team: team.elo,
        reverse=True
    )


if __name__ == "__main__":
    ranking = get_power_ranking()

    for position, team in enumerate(ranking, start=1):
        print(
            f"{position:02d} | "
            f"{team.name:<3} | "
            f"ELO {team.elo}"
        )