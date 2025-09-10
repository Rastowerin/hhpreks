import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("HH_CLIENT_ID")
CLIENT_SECRET = os.getenv("HH_CLIENT_SECRET")
REDIRECT_URI = ""
AUTH_CODE = os.getenv("AUTH_CODE")
TOKEN = os.getenv("TOKEN")
RESUME = os.getenv("RESUME")

def get_auth_url():
    return f"https://hh.ru/oauth/authorize?response_type=code&client_id={CLIENT_ID}"

def get_access_token(auth_code, redirect_uri) -> str:
    url = "https://hh.ru/oauth/token"    

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": redirect_uri,
        "code": auth_code
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(
            f"Ошибка получения токена: {response.status_code}, {response.text}"
        )


def search_vacancies(text: str) -> list[dict]:
    url = "https://api.hh.ru/vacancies"
    page = 0
    per_page = 100 
    results = []

    while True:
        print(f"on page {page}")
        params = {
            "text": text,
#             "search_field": "name",
            "page": page,
            "per_page": per_page
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Ошибка поиска: {response.status_code}, {response.text}")

        data = response.json()
        items = data.get("items", [])
        if not items:
            break

        results.extend(items)
        print(f"{len(results)} vacancies found\n")

        if page >= data.get("pages", 0) - 1:
            break

        page += 1

    return results

def apply_to_vacancy(access_token, vacancy_id, resume_id, message: str = None):
    url = "https://api.hh.ru/negotiations"

    payload = {
        "vacancy_id": vacancy_id,
        "resume_id": resume_id
    }
    if message:
        payload["message"] = message

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.status_code
