import argparse
from tracker import HabitTracker


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Habit Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("add", help="Add habit")
    subparsers.add_parser("list", help="List habits")

    complete_parser = subparsers.add_parser("complete", help="Mark habit complete")
    complete_parser.add_argument("habit_id", type=int)

    delete_parser = subparsers.add_parser("delete", help="Delete habit")
    delete_parser.add_argument("habit_id", type=int)

    args = parser.parse_args()
    tracker = HabitTracker()

    if args.command == "add":
        name = input("Habit name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        freq = input("Frequency (daily/weekly): ").strip().lower()
        if freq not in ("daily", "weekly"):
            print("Invalid frequency. Must be 'daily' or 'weekly'.")
            return

        h = tracker.add_habit(name, freq)
        print(f"Added habit #{h.id}: {h.name}")

    elif args.command == "list":
        habits = tracker.get_all_habits()
        if not habits:
            print("No habits found. Add one with: python main.py add")
            return

        print("\nID   Name                 Freq     Done Today  Streak")
        print("-" * 52)
        for h in habits:
            done = "Yes" if h.is_completed_today() else "No"
            print(f"{h.id:<4} {h.name:<20} {h.frequency:<8} {done:<11} {h.calculate_streak()}")
        print()

    elif args.command == "complete":
        res = tracker.complete_habit(args.habit_id)
        if res is None:
            print(f"No habit found with ID {args.habit_id}.")
        elif res:
            print(f"Habit #{args.habit_id} marked complete for today!")
        else:
            print(f"Habit #{args.habit_id} was already completed today.")

    elif args.command == "delete":
        if tracker.delete_habit(args.habit_id):
            print(f"Deleted habit #{args.habit_id}.")
        else:
            print(f"No habit found with ID {args.habit_id}.")


if __name__ == "__main__":
    main()