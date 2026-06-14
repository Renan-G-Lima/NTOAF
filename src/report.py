from src.prediction_repository import PredictionRepository


def prediction_report() -> None:

    predictions = PredictionRepository.get_all()

    total = len(predictions)

    correct = sum(
        1
        for prediction in predictions
        if prediction.correct is True
    )

    incorrect = sum(
        1
        for prediction in predictions
        if prediction.correct is False
    )

    pending = sum(
        1
        for prediction in predictions
        if prediction.correct is None
    )

    accuracy = (
        (correct / (correct + incorrect)) * 100
        if (correct + incorrect) > 0
        else 0
    )

    print("\n===== NTOAF REPORT =====")
    print(f"Total Predictions : {total}")
    print(f"Correct           : {correct}")
    print(f"Incorrect         : {incorrect}")
    print(f"Pending           : {pending}")
    print(f"Accuracy          : {accuracy:.2f}%")