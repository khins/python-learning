# 12_github_analyzer.py
from dataclasses import dataclass
import logging
from pathlib import Path

import requests


LOG_FILE = Path(__file__).resolve().parent.parent / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)


@dataclass
class Repo:
    name: str
    stars: int


@dataclass
class RepoSummary:
    total_repos: int
    total_stars: int
    most_starred_name: str
    most_starred_stars: int


class InvalidUsernameError(Exception):
    pass


class RepoFetchError(Exception):
    pass


def validate_username(username: str) -> str:
    cleaned_username = username.strip()

    if not cleaned_username:
        raise InvalidUsernameError("GitHub username cannot be empty.")

    return cleaned_username


def fetch_repo_data(username: str) -> list[dict]:
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code if error.response is not None else None

        if status_code == 404:
            logging.error("GitHub user '%s' was not found.", username)
            raise RepoFetchError(f"User '{username}' does not exist on GitHub.") from error
        elif status_code == 403:
            logging.error(
                "GitHub API access was denied or rate-limited for user '%s'.",
                username,
            )
            raise RepoFetchError(
                "GitHub denied the request or the API rate limit was reached. "
                "Please try again later."
            ) from error
        else:
            logging.error(
                "GitHub API returned HTTP %s for user '%s'.",
                status_code,
                username,
            )
            raise RepoFetchError(
                f"GitHub returned an unexpected HTTP error: {status_code}."
            ) from error
    except requests.exceptions.RequestException as error:
        logging.error("Network error while fetching repos: %s", error)
        raise RepoFetchError(
            "A network error happened while contacting GitHub. Check your "
            "internet connection and try again."
        ) from error

    logging.info("Fetched repo data for username: %s", username)
    return response.json()


def parse_repos(repo_data: list[dict]) -> list[Repo]:
    repos = []

    for repo in repo_data:
        repos.append(
            Repo(
                name=repo.get("name", "Unknown"),
                stars=repo.get("stargazers_count", 0),
            )
        )

    return repos


def summarize_repos(repos: list[Repo]) -> RepoSummary | None:
    if not repos:
        return None

    total_repos = len(repos)
    total_stars = sum(repo.stars for repo in repos)
    most_starred = max(repos, key=lambda repo: repo.stars)

    return RepoSummary(
        total_repos=total_repos,
        total_stars=total_stars,
        most_starred_name=most_starred.name,
        most_starred_stars=most_starred.stars,
    )


def display_summary(summary: RepoSummary | None) -> None:
    if summary is None:
        logging.warning("No repo data available to summarize.")
        print("No repo data to analyze.")
        return

    print("\n--- Repo Analytics ---")
    print("Total repos:", summary.total_repos)
    print("Total stars:", summary.total_stars)
    print("Most starred repo:", summary.most_starred_name)
    print("Stars on top repo:", summary.most_starred_stars)


def main() -> None:
    try:
        username = validate_username(input("Enter GitHub username: "))
        repo_data = fetch_repo_data(username)
        repos = parse_repos(repo_data)
        summary = summarize_repos(repos)
        display_summary(summary)
    except InvalidUsernameError as error:
        logging.error("Invalid input: %s", error)
        print(error)
    except RepoFetchError as error:
        print(error)


# Main execution
if __name__ == "__main__":
    main()
