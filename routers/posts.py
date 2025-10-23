from fastapi import APIRouter, Depends, HTTPException
from database import fake_posts_db
from schemas import PostCreate, Post, Comment, Like, User
from dependencies import get_current_user
from uuid import uuid4, UUID
from datetime import datetime

router = APIRouter()

@router.post("/posts/", response_model=Post)
def create_post(post: PostCreate, current_user: User = Depends(get_current_user)):
    new_post = {
        "id": uuid4(),
        "text": post.text,
        "owner_id": current_user.id,
        "created_at": datetime.utcnow()
    }
    fake_posts_db.append(new_post)
    return new_post

@router.get("/posts/", response_model=list[Post])
def get_all_posts():
    return fake_posts_db

@router.delete("/posts/{post_id}")
def delete_post(post_id: UUID, current_user: User = Depends(get_current_user)):
    for post in fake_posts_db:
        if post["id"] == post_id:
            if post["owner_id"] != current_user.id:
                raise HTTPException(status_code=403, detail="Not authorized to delete this post")
            fake_posts_db.remove(post)
            return {"detail": "Post deleted"}
    raise HTTPException(status_code=404, detail="Post not found")

@router.post("/like")
def like_post(like: Like, current_user: User = Depends(get_current_user)):
    return {"detail": f"User {current_user.id} liked post {like.post_id}"}

@router.post("/comment")
def comment_post(comment: Comment, current_user: User = Depends(get_current_user)):
    return {"detail": f"User {current_user.id} commented on post {comment.post_id}: {comment.text}"}
