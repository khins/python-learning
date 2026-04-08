# Task Tracker Capstone

This project is the long-running mini-project for the 8-week plan.

## Features

- add tasks
- list tasks
- complete tasks
- delete tasks
- save/load JSON
- custom validation and storage errors
- optional `rich` output when installed

## Commands

```bash
./venv/bin/python task-tracker/main.py add "Review dataclasses" --priority high
./venv/bin/python task-tracker/main.py list
./venv/bin/python task-tracker/main.py complete 1
./venv/bin/python task-tracker/main.py delete 1
```

## Notes

- Data is stored in `task-tracker/tasks.json` by default.
- Set `TASK_TRACKER_DATA` if you want a different file path.
- The code is intentionally small and readable so you can study it.
