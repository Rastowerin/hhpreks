import json

from funcs import search_vacancies

if __name__ == "__main__":
    res = search_vacancies("golang")
    with open("vacancies.json", "w") as f:
            f.write(json.dumps(res))
