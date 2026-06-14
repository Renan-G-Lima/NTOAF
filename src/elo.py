def expected_score(
    rating_a: float,
    rating_b: float,
) -> float:

    return 1 / (
        1 + 10 ** (
            (rating_b - rating_a) / 400
        )
    )


def update_elo(
    winner_rating: float,
    loser_rating: float,
    k_factor: int = 20,
) -> tuple[float, float]:

    winner_expected = expected_score(
        winner_rating,
        loser_rating,
    )

    loser_expected = expected_score(
        loser_rating,
        winner_rating,
    )

    new_winner = (
        winner_rating
        + k_factor
        * (1 - winner_expected)
    )

    new_loser = (
        loser_rating
        + k_factor
        * (0 - loser_expected)
    )

    return (
        round(new_winner, 2),
        round(new_loser, 2),
    )
