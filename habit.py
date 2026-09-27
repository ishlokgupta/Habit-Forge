from datetime import date, timedelta


class Habit:
    """Represents one habit and the dates it was completed."""

    VALID_FREQUENCIES = {"daily", "weekly"}

    def __init__(self, habit_id, name, frequency, completed_dates=None):
        self.id = habit_id
        self.name = name
        self.frequency = frequency
        self.completed_dates = completed_dates or []

    def mark_complete(self):
        """Mark this habit as completed for today's date."""
        today = date.today().isoformat()

        if today not in self.completed_dates:
            self.completed_dates.append(today)
            return True

        return False

    def calculate_streak(self):
        """Calculate the current completion streak for this habit."""
        if not self.completed_dates:
            return 0

        completion_dates = self._get_valid_completion_dates()

        if self.frequency == "daily":
            return self._calculate_daily_streak(completion_dates)

        return self._calculate_weekly_streak(completion_dates)

    def to_dict(self):
        """Convert this Habit object into a dictionary for JSON storage."""
        return {
            "id": self.id,
            "name": self.name,
            "frequency": self.frequency,
            "completed_dates": self.completed_dates,
        }

    @classmethod
    def from_dict(cls, habit_data):
        """Create a Habit object from saved JSON data."""
        return cls(
            habit_id=habit_data["id"],
            name=habit_data["name"],
            frequency=habit_data["frequency"],
            completed_dates=habit_data.get("completed_dates", []),
        )

    def is_completed_today(self):
        """Return True if the habit has already been completed today."""
        return date.today().isoformat() in self.completed_dates

    def _get_valid_completion_dates(self):
        """Return saved dates as date objects, ignoring invalid entries."""
        valid_dates = []

        for completion_date in self.completed_dates:
            try:
                valid_dates.append(date.fromisoformat(completion_date))
            except ValueError:
                # Bad saved dates should not crash the whole app.
                continue

        return set(valid_dates)

    def _calculate_daily_streak(self, completion_dates):
        """Count consecutive completed days ending today or yesterday."""
        current_day = date.today()

        # If today is not done yet, yesterday can still be the active streak.
        if current_day not in completion_dates:
            current_day -= timedelta(days=1)

        streak = 0

        while current_day in completion_dates:
            streak += 1
            current_day -= timedelta(days=1)

        return streak

    def _calculate_weekly_streak(self, completion_dates):
        """Count consecutive completed weeks ending this week or last week."""
        completed_weeks = {
            completion_date.isocalendar()[:2]
            for completion_date in completion_dates
        }

        current_week_start = self._start_of_week(date.today())
        current_week = current_week_start.isocalendar()[:2]

        # If this week is not done yet, last week can still be the streak.
        if current_week not in completed_weeks:
            current_week_start -= timedelta(weeks=1)

        streak = 0

        while current_week_start.isocalendar()[:2] in completed_weeks:
            streak += 1
            current_week_start -= timedelta(weeks=1)

        return streak

    def _start_of_week(self, current_date):
        """Return the Monday for the week containing current_date."""
        return current_date - timedelta(days=current_date.weekday())