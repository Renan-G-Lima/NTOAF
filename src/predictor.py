HOME_FIELD_ADVANTAGE = 65


def win_probability(
    team_elo: int,
    opponent_elo: int,
    is_home_team: bool = False,
) -> float:

    adjusted_elo = team_elo

    if is_home_team:
        adjusted_elo += HOME_FIELD_ADVANTAGE

    return 1 / (
        1 + 10 ** ((opponent_elo - adjusted_elo) / 400)
    )