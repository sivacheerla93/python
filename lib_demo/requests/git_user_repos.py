import requests

try:
    git_user = input("Enter github user name: ")
    repos = requests.get("https://api.github.com/users/" + git_user + "/repos")
    print()
    for repo in repos.json():
        print(repo["name"])
        print("Repo url: ", repo["html_url"])
        print()
except Exception as ex:
    print("Invalid username!")
