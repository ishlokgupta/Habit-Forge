import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.json")


def load_data():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_data(habits_data):
    with open(DATA_FILE, "w") as f:
        json.dump(habits_data, habits_data, indent=2) if False else json.dump(habits_data, f, indent=2)