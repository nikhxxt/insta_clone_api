from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class Like(BaseModel):
    post_id: UUID
    user_id: int

class Comment(BaseModel):
    post_id: UUID
    user_id: int
    text: str = Field(..., min_length=1, max_length=300)
