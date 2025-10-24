# main.py
from fastapi import FastAPI
from routers import posts

app = FastAPI()
app.include_router(posts.router)

# Optional: Only needed for local development
# Uncomment if you want to run with `python main.py`
# But Render does NOT need this block
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
