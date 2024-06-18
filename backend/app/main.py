from fastapi import FastAPI
from .database import engine, Base
from .routers import anime, user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(anime.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Aniverce API"}
