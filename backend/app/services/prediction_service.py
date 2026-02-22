import random


def predict_visit(place_id: int, service_type: str, hour: int, day_of_week: int):

    # basic logic simulation (temporary until ML model)
    base_wait = random.randint(5, 60)

    # rush hours simulation
    if 11 <= hour <= 14:
        base_wait += 20

    # monday rush
    if day_of_week == 0:
        base_wait += 15

    success_probability = max(10, 100 - base_wait)

    if success_probability > 70:
        decision = "GO NOW"
    elif success_probability > 40:
        decision = "RISKY"
    else:
        decision = "GO LATER"

    return {
        "decision": decision,
        "expected_wait_time": base_wait,
        "success_probability": success_probability
    }