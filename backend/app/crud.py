# backend/app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas
import requests

JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com"

def get_user(db: Session, user_id: int):
    try:
        response = requests.get(f"{JSONPLACEHOLDER_URL}/users/{user_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
        return None

def create_user(db: Session, user: schemas.UserCreate):
    try:
        response = requests.post(f"{JSONPLACEHOLDER_URL}/users/", json={"email": user.email})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
        return None

def get_anime(db: Session, anime_id: int):
    try:
        response = requests.get(f"{JSONPLACEHOLDER_URL}/posts/{anime_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
        return None

def create_anime(db: Session, anime: schemas.AnimeCreate):
    try:
        response = requests.post(f"{JSONPLACEHOLDER_URL}/posts/", json={"title": anime.title, "body": anime.description, "userId": anime.rating})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
        return None
