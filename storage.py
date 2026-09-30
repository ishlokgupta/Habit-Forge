import json
from pathlib import Path

# Always locate data.json relative to this script, so running from another folder won't break paths
DATA_FILE = Path(__file__).with_name("data.json")


def load_data():
    # If starting fresh on a new setup, default to an empty list
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            # Make sure we actually got a list back before returning
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        # If the file gets corrupted or messed up manually, fail gracefully
        return []


def save_data(habits_data):
    # Overwrite data.json with the updated habit list using 2-space formatting for readability
    with open(DATA_FILE, "w") as f:
        json.dump(habits_data, f, indent=2)