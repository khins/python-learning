"""
Beginner PostgreSQL example using psycopg.

This script expects a DATABASE_URL environment variable, for example:

    export DATABASE_URL="postgresql://myuser:mypassword@localhost:5432/my_first_python_app"

Then run:

    ../venv/bin/python python-language/postgres_basics.py
"""

from __future__ import annotations

import os

import psycopg


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError(
            "DATABASE_URL is not set. Example: "
            "postgresql://myuser:mypassword@localhost:5432/my_first_python_app"
        )
    return database_url


def run_demo() -> None:
    database_url = get_database_url()

    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS lessons (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    duration_minutes INTEGER NOT NULL,
                    completed BOOLEAN NOT NULL DEFAULT FALSE
                )
                """
            )

            cur.execute(
                """
                INSERT INTO lessons (title, duration_minutes, completed)
                VALUES (%s, %s, %s)
                """,
                ("PostgreSQL Basics", 45, False),
            )

            cur.execute(
                """
                SELECT id, title, duration_minutes, completed
                FROM lessons
                ORDER BY id
                """
            )
            rows = cur.fetchall()

    print("Saved lessons:")
    for row in rows:
        print(row)


if __name__ == "__main__":
    run_demo()
