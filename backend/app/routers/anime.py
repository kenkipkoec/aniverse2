from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/animes",
    tags=["animes"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Anime)
def create_anime(anime: schemas.AnimeCreate, db: Session = Depends(get_db)):
    return crud.create_anime(db=db, anime=anime)

@router.get("/{anime_id}", response_model=schemas.Anime)
def read_anime(anime_id: int, db: Session = Depends(get_db)):
    db_anime = crud.get_anime(db, anime_id=anime_id)
    if db_anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    return db_anime
