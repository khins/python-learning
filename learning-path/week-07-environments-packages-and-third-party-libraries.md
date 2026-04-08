# Week 7: Environments, Packages, and Third-Party Libraries

## Learn

- `venv`
- `pip install`
- dependency isolation
- standard library vs installed packages

## Practice File

Run [week_07_environments_and_packages.py](/home/kevin/projects/my-first-python-app/python-language/weekly-practice/week_07_environments_and_packages.py).

## Project Work

- Study the optional rich support in [cli.py](/home/kevin/projects/my-first-python-app/task-tracker/task_tracker/cli.py)
- Try installing `rich` in your venv if you want colored output

## Commands

```bash
./venv/bin/python -m pip install rich
./venv/bin/python task-tracker/main.py list
./venv/bin/python -m pip freeze
```

## Review Check

- Can you explain why global installs are risky?
- Can you identify which imports come from the standard library?
