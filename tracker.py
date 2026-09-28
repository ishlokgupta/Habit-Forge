from habit import Habit
from storage import load_data, save_data


class HabitTracker:
    def __init__(self):
        self.habits = self._load_habits()

    def add_habit(self, name, frequency):
        next_id = max([h.id for h in self.habits], default=0) + 1
        habit = Habit(next_id, name, frequency)
        self.habits.append(habit)
        self.save()
        return habit

    def get_all_habits(self):
        return self.habits

    def get_habit(self, habit_id):
        for h in self.habits:
            if h.id == habit_id:
                return h
        return None

    def complete_habit(self, habit_id):
        habit = self.get_habit(habit_id)
        if not habit:
            return None

        res = habit.mark_complete()
        self.save()
        return res

    def delete_habit(self, habit_id):
        habit = self.get_habit(habit_id)
        if not habit:
            return False

        self.habits.remove(habit)
        self.save()
        return True

    def save(self):
        save_data([h.to_dict() for h in self.habits])

    def _load_habits(self):
        habits = []
        for item in load_data():
            try:
                habits.append(Habit.from_dict(item))
            except (KeyError, TypeError):
                pass
        return habits