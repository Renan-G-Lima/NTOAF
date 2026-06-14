def implied_probability(decimal_odds: float) -> float:
    return 1 / decimal_odds


def edge(
    model_probability: float,
    decimal_odds: float,
) -> float:

    market_probability = implied_probability(
        decimal_odds
    )

    return model_probability - market_probability

def confidence_score(
    model_probability: float,
    edge_value: float,
) -> float:

    return (
        model_probability * 100
        + edge_value * 100
    )