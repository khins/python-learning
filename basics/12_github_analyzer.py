# 12_github_analyzer.py
from dataclasses import dataclass

import requests


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


def fetch_repo_data(username: str) -> list[dict]:
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        print("Could not fetch repos.")
        return []

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
        print("No repo data to analyze.")
        return

    print("\n--- Repo Analytics ---")
    print("Total repos:", summary.total_repos)
    print("Total stars:", summary.total_stars)
    print("Most starred repo:", summary.most_starred_name)
    print("Stars on top repo:", summary.most_starred_stars)


def main() -> None:
    username = input("Enter GitHub username: ")
    repo_data = fetch_repo_data(username)
    repos = parse_repos(repo_data)
    summary = summarize_repos(repos)
    display_summary(summary)


# Main execution
if __name__ == "__main__":
    main()
