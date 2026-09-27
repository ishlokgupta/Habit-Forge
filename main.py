import argparse

from habit import Habit
from tracker import HabitTracker


def main():
    parser = argparse.ArgumentParser(
        description="HabitForge: a simple command-line habit tracker."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("add", help="Add a new habit")
    subparsers.add_parser("list", help="List all habits")

    complete_parser = subparsers.add_parser(
        "complete",
        help="Mark a habit as completed today",
    )
    complete_parser.add_argument("habit_id", type=int, help="ID of the habit")

    delete_parser = subparsers.add_parser("delete", help="Delete a habit")
    delete_parser.add_argument("habit_id", type=int, help="ID of the habit")

    args = parser.parse_args()
    tracker = HabitTracker()

    if args.command == "add":
        handle_add(tracker)
    elif args.command == "list":
        handle_list(tracker)
    elif args.command == "complete":
        handle_complete(tracker, args.habit_id)
    elif args.command == "delete":
        handle_delete(tracker, args.habit_id)


def handle_add(tracker):
    name = input("Habit name: ").strip()

    if not name:
        print("Habit name cannot be empty.")
        return

    frequency = input("Frequency (daily/weekly): ").strip().lower()

    if frequency not in Habit.VALID_FREQUENCIES:
        print("Invalid frequency. Please enter 'daily' or 'weekly'.")
        return

    habit = tracker.add_habit(name, frequency)
    print(f"Added habit #{habit.id}: {habit.name}")


def handle_list(tracker):
    habits = tracker.get_all_habits()

    if not habits:
        print("No habits found. Add your first habit with: python main.py add")
        return

    print()
    print("ID | Name | Frequency | Completed Today | Current Streak")
    print("-" * 58)

    for habit in habits:
        completed_today = "Yes" if habit.is_completed_today() else "No"
        streak = habit.calculate_streak()
        print(
            f"{habit.id} | {habit.name} | {habit.frequency} | "
            f"{completed_today} | {streak}"
        )

    print()


def handle_complete(tracker, habit_id):
    result = tracker.complete_habit(habit_id)

    if result is None:
        print(f"No habit found with ID {habit_id}.")
    elif result:
        print(f"Habit #{habit_id} marked as completed for today.")
    else:
        print(f"Habit #{habit_id} was already completed today.")


def handle_delete(tracker, habit_id):
    was_deleted = tracker.delete_habit(habit_id)

    if was_deleted:
        print(f"Habit #{habit_id} deleted.")
    else:
        print(f"No habit found with ID {habit_id}.")


if __name__ == "__main__":
    main()
