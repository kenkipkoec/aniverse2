from pydantic import BaseModel

class AnimeBase(BaseModel):
    title: str
    description: str
    rating: int

class AnimeCreate(AnimeBase):
    pass

class Anime(AnimeBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str  # Define the password attribute

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
