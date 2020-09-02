# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.
import json

import requests

host = "https://api.github.com"
timeout_s = 7
user = "esineokov"


def get_user_repos(user):
    response = requests.get(f"{host}/users/{user}/repos", timeout=timeout_s)
    with open("user_repos.json", "w") as file:
        json.dump(response.json(), file, indent=1)


get_user_repos(user)
