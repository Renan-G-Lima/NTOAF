def is_bet_recommended(
    probability: float,
    threshold: float = 0.60,
) -> bool:

    return probability >= threshold