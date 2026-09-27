import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("data.json")


def load_data():
    """Load habit dictionaries from the JSON data file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Warning: data.json is not valid JSON. Starting with no habits.")
        return []

    if not isinstance(data, list):
        print("Warning: data.json should contain a list. Starting with no habits.")
        return []

    return data


def save_data(habits_data):
    """Save habit dictionaries to the JSON data file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(habits_data, file, indent=4)
