from datetime import date, timedelta


class Habit:
    def __init__(self, habit_id, name, frequency, dates=None):
        self.id = habit_id
        self.name = name
        self.frequency = frequency
        self.dates = dates or []

    def mark_complete(self):
        today = date.today().isoformat()
        if today not in self.dates:
            self.dates.append(today)
            return True
        return False

    def is_completed_today(self):
        return date.today().isoformat() in self.dates

    def calculate_streak(self):
        if not self.dates:
            return 0

        # Parse stored ISO date strings
        valid_dates = set()
        for d in self.dates:
            try:
                valid_dates.add(date.fromisoformat(d))
            except ValueError:
                pass

        if self.frequency == "daily":
            return self._daily_streak(valid_dates)
        return self._weekly_streak(valid_dates)

    def _daily_streak(self, valid_dates):
        curr = date.today()
        if curr not in valid_dates:
            curr -= timedelta(days=1)

        streak = 0
        while curr in valid_dates:
            streak += 1
            curr -= timedelta(days=1)
        return streak

    def _weekly_streak(self, valid_dates):
        weeks = {d.isocalendar()[:2] for d in valid_dates}

        # Start of current week (Monday)
        today = date.today()
        curr_monday = today - timedelta(days=today.weekday())

        if curr_monday.isocalendar()[:2] not in weeks:
            curr_monday -= timedelta(weeks=1)

        streak = 0
        while curr_monday.isocalendar()[:2] in weeks:
            streak += 1
            curr_monday -= timedelta(weeks=1)
        return streak

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "frequency": self.frequency,
            "completed_dates": self.dates,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["frequency"], data.get("completed_dates"))