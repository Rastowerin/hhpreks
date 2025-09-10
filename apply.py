import json

from funcs import apply_to_vacancy, get_access_token, AUTH_CODE, RESUME, REDIRECT_URI

def new_token():
    token = get_access_token(AUTH_CODE, REDIRECT_URI)
    with open('token.txt', 'w') as f:
        f.write(token)
    return token

def get_token():
    with open('token.txt', 'r') as f:
        token = f.readline()
    return token


if __name__ == "__main__":

    with open("vacancies.json", "r") as f:
        vacancies = json.loads(f.read())

    try:
        token = get_token()
    except Exception:
        token = new_token()

    for vacancy in vacancies:

        retry = True
        try:
            res = apply_to_vacancy(token, vacancy['id'], RESUME)
        except Exception as e:
            if retry:
                token = new_token()
                res = apply_to_vacancy(token, vacancy['id'], RESUME)
                retry = False
            else:
                raise e

        print(res)

