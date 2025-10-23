# dependencies.py
from fastapi import Header, HTTPException, Depends
from database import fake_users_db
from schemas import User

def get_current_user(x_user_id: int = Header(...)) -> User:
    user = fake_users_db.get(x_user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(id=x_user_id, username=user["username"])
