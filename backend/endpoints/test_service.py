import requests
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("API_KEY")
search_by_name = os.getenv("SEARCH_NAME")
search_by_id = os.getenv("SEARCH_ID")

# Установка заголовков с ключом API
headers = {"X-API-KEY": api_key}

def get_movies_by_name(query):
    params = {'query': query}
    try:
        response = requests.get(
            search_by_name,
            headers=headers,
            params=params
        )
        response.raise_for_status()  # Проверка на ошибки HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_movies_by_id(movie_id):
    try:
        response = requests.get(
            f'{search_by_id}{movie_id}',
            headers=headers
        )
        response.raise_for_status()  # Проверка на ошибки HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Выполняем поиск фильмов
movies = get_movies_by_name('Сопрано')

if movies is not None and "docs" in movies and len(movies["docs"]) > 0:
    # Если фильм найден, получаем факты о нем
    facts = get_movies_by_id(movies["docs"][0]["id"])
    if facts:
        print(facts["facts"][:3])
    else:
        print("Данные о фактах недоступны или отсутствуют.")
else:
    print("Фильм не найден.")
