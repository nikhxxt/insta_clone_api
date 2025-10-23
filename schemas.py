# schemas.py
from pydantic import BaseModel

class PostCreate(BaseModel):
    text: str

class Post(BaseModel):
    id: int
    text: str
    owner_id: int

class User(BaseModel):
    id: int
    username: str

class Like(BaseModel):
    post_id: int
    user_id: int

class Comment(BaseModel):
    post_id: int
    user_id: int
    text: str
