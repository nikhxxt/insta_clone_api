# main.py
from fastapi import FastAPI
from routers import posts

app = FastAPI()
app.include_router(posts.router)
