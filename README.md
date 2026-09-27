# HabitForge

HabitForge is a beginner-friendly command-line habit tracker built with Python.
It lets you create habits, view them, mark them as completed, track streaks, and
delete habits when you no longer need them.

## Features

- Add daily or weekly habits
- List all saved habits
- Mark a habit as completed for today
- Track current daily and weekly streaks
- Delete habits by ID
- Store data locally in a JSON file
- Handle missing or invalid `data.json` gracefully

## Project Structure

```text
habit-forge/
|-- main.py
|-- habit.py
|-- tracker.py
|-- storage.py
|-- data.json
|-- README.md
|-- requirements.txt
`-- .gitignore
```

## Installation

1. Clone or download this project.
2. Open a terminal in the `habit-forge` folder.
3. Make sure Python 3 is installed:

```bash
python --version
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

HabitForge currently uses only the Python standard library, so there are no
external packages to install.

## Usage

Add a new habit:

```bash
python main.py add
```

List all habits:

```bash
python main.py list
```

Mark a habit as completed:

```bash
python main.py complete 1
```

Delete a habit:

```bash
python main.py delete 1
```

## How Streaks Work

Daily habits count consecutive completed days. If today has not been completed
yet, yesterday can still count as the active streak.

Weekly habits count consecutive completed calendar weeks. If this week has not
been completed yet, last week can still count as the active streak.

## Future Improvements

- Add unit tests
- Add edit habit command
- Add notes for each completion
- Add monthly habits
- Add habit categories
- Show longest streak
- Export habit data to CSV
- Add a richer terminal table display