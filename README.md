# Python Learning

This repository is now organized as a guided 8-week Python learning path.

## Start Here

- Read [learning-path/README.md](/home/kevin/projects/my-first-python-app/learning-path/README.md)
- Work through one weekly guide at a time
- Use [python-language/weekly-practice](/home/kevin/projects/my-first-python-app/python-language/weekly-practice) for short concept files
- Build on the capstone project in [task-tracker/README.md](/home/kevin/projects/my-first-python-app/task-tracker/README.md)

## Repository Layout

- `basics/`, `loops/`, `functions/`, `data-structures/`: earlier practice work
- `python-language/`: topic-focused language demos
- `python-language/weekly-practice/`: one short concept file for each week
- `learning-path/`: week-by-week learning guides and checkpoints
- `task-tracker/`: the growing command-line project for Weeks 2-8
- `tests/`: automated tests for the task tracker

## Running The Capstone Project

Use the repo virtual environment:

```bash
./venv/bin/python task-tracker/main.py --help
./venv/bin/python task-tracker/main.py add "Finish Python practice"
./venv/bin/python task-tracker/main.py list
```

## Running Tests

```bash
./venv/bin/python -m unittest discover -s tests -v
```
