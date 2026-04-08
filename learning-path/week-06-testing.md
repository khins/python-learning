# Week 6: Testing

## Learn

- `unittest`
- testing pure functions
- testing raised exceptions
- testing file-backed code with temporary directories

## Practice File

Run [week_06_testing_basics.py](/home/kevin/projects/my-first-python-app/python-language/weekly-practice/week_06_testing_basics.py).

## Project Work

- Read [tests/test_task_tracker.py](/home/kevin/projects/my-first-python-app/tests/test_task_tracker.py)
- Run the test suite
- Add one extra test of your own

## Commands

```bash
./venv/bin/python -m unittest discover -s tests -v
```

## Review Check

- Can you test both the happy path and failure path?
- Can you explain why temporary directories are useful in tests?
