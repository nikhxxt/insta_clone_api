from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

# ---------- Post Models ----------
class PostCreate(BaseModel):
    text: str = Field(..., min_length=1, description="Content of the post")

class Post(BaseModel):
    id: UUID
    text: str
    owner_id: int
    created_at: datetime

# ---------- User Model ----------
class User(BaseModel):
    id: int
    username: str

# ---------- Like Models ----------
class Like(BaseModel):
    post_id: UUID
    user_id: int

class LikeResponse(BaseModel):
    post_id: UUID
    liked_by: User
    liked_at: datetime

# ---------- Comment Models ----------
class Comment(BaseModel):
    post_id: UUID
    user_id: int
    text: str = Field(..., min_length=1, max_length=300, description="Comment text (1–300 characters)")


