from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class PostCreate(BaseModel):
    text: str = Field(..., min_length=1)

class Post(BaseModel):
    id: UUID
    text: str
    owner_id: int
    created_at: datetime

class User(BaseModel):
    id: int
    username: str

class Like(BaseModel):
    post_id: UUID
    user_id: int

class Comment(BaseModel):
    post_id: UUID
    user_id: int
    text: str = Field(..., min_length=1, max_length=300)
