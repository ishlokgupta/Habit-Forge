from habit import Habit
from storage import load_data, save_data


class HabitTracker:
    """Handles habit actions such as add, list, complete, and delete."""

    def __init__(self):
        self.habits = self._load_habits()

    def add_habit(self, name, frequency):
        """Create a new habit and save it."""
        habit_id = self._get_next_id()
        habit = Habit(habit_id, name, frequency)
        self.habits.append(habit)
        self.save()
        return habit

    def get_all_habits(self):
        """Return all habits."""
        return self.habits

    def complete_habit(self, habit_id):
        """Mark a habit as completed today."""
        habit = self.find_habit_by_id(habit_id)

        if habit is None:
            return None

        was_updated = habit.mark_complete()
        self.save()
        return was_updated

    def delete_habit(self, habit_id):
        """Delete a habit by ID."""
        habit = self.find_habit_by_id(habit_id)

        if habit is None:
            return False

        self.habits.remove(habit)
        self.save()
        return True

    def find_habit_by_id(self, habit_id):
        """Find and return one habit by ID."""
        for habit in self.habits:
            if habit.id == habit_id:
                return habit

        return None

    def save(self):
        """Save all habits to the JSON data file."""
        habits_data = [habit.to_dict() for habit in self.habits]
        save_data(habits_data)

    def _load_habits(self):
        """Load saved habit dictionaries and convert them into Habit objects."""
        habits = []

        for habit_data in load_data():
            try:
                habits.append(Habit.from_dict(habit_data))
            except (KeyError, TypeError):
                # Skip badly formatted records instead of crashing the app.
                continue

        return habits

    def _get_next_id(self):
        """Return the next available habit ID."""
        if not self.habits:
            return 1

        return max(habit.id for habit in self.habits) + 1
