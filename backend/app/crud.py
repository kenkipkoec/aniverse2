# backend/app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notsecure"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_anime(db: Session, anime_id: int):
    return db.query(models.Anime).filter(models.Anime.id == anime_id).first()

def create_anime(db: Session, anime: schemas.AnimeCreate):
    db_anime = models.Anime(title=anime.title, description=anime.description, rating=anime.rating)
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime
