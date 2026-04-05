# 12_github_analyzer.py
import requests

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        print("Could not fetch repos.")
        return []

    return response.json()

def analyze_repos(repos):
    if not repos:
        print("No repo data to analyze.")
        return

    total_repos = len(repos)
    total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)

    most_starred = max(repos, key=lambda r: r.get("stargazers_count", 0))

    print("\n--- Repo Analytics ---")
    print("Total repos:", total_repos)
    print("Total stars:", total_stars)
    print("Most starred repo:", most_starred.get("name"))
    print("Stars on top repo:", most_starred.get("stargazers_count"))

# Main execution
if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    repos = fetch_repos(username)
    analyze_repos(repos)