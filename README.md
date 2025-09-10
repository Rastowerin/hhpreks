## Установка зависимостей

1. Установите uv (если еще не установлен):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Создайте виртуальное окружение и установите зависимости:
   ```bash
   uv sync
   ```

3. Активируйте виртуальное окружение:
   ```bash
   source .venv/bin/activate
   ```

## Использование

1. Нужны HH_CLIENT_ID и HH_CLIENT_SECRET
2. Идешь по ссылке hh.ru/oauth/authorize?response_type=code&client_id=<HH_CLIENT_ID>, тебя редиректнет на урл с параметром code, его ложи в AUTH_CODE в .env
3. python search.py - генерит json с вакансиями(укажи нужное слово, если надо то в funcs.py закомменитруй "search_field": "name")
4. python apply.py - аплаится на все эти вакансии

