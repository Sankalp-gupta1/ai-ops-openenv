import random

def generate_log():
    logs = [
        "database timeout error",
        "cpu overload detected",
        "memory leak suspected",
        "service running normally"
    ]
    return random.choice(logs)

def generate_metrics(level):
    if level == "easy":
        return 90, 40, 10
    elif level == "medium":
        return 60, 85, 20
    else:
        return 95, 90, 100