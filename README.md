
# 📸 InstaClone API

A modular FastAPI backend simulating Instagram-style post activities. Built for clarity, authentication flow demonstration, and cloud deployment. Uses in-memory storage and header-based user simulation for simplicity and speed.

---

## 📚 Table of Contents
- 🚀 Features
- 📬 Authentication Flow
- 📝 Post Endpoints
- ❤️ Like & 💬 Comment Endpoints
- 🧪 Sample Users
- 🌐 Live Demo
- 🛠 Tech Stack
- 🧪 Run Locally
- 📁 File Structure
- 📜 License

---

## 🚀 Features
✅ Header-based user authentication (`X-User-ID`)  
📝 Create, view, and delete posts  
🔐 Ownership checks for delete operations  
❤️ Like posts  
💬 Comment on posts  
📦 Modular structure with FastAPI routers and dependencies  
🧪 In-memory DB for quick prototyping  

---

## 📬 Authentication Flow
All protected endpoints require a valid `X-User-ID` header.

**Example:**
```
X-User-ID: 1
```

If the user ID is not found in `fake_users_db`, the API returns a `404 Not Found` error.

---

## 📝 Post Endpoints

### ➕ `POST /posts/`
Create a new post.

**Headers:**
```
X-User-ID: 1
```

**Body:**
```json
{
  "text": "Hello from InstaClone!"
}
```

**Response:**
```json
{
  "id": "uuid",
  "text": "Hello from InstaClone!",
  "owner_id": 1,
  "created_at": "2025-10-24T18:20:00.123Z",
  "likes": [],
  "comments": []
}
```

---

### 📄 `GET /posts/`
Returns all posts.

**Response:**
```json
[
  {
    "id": "uuid",
    "text": "Hello from InstaClone!",
    "owner_id": 1,
    "created_at": "2025-10-24T18:20:00.123Z",
    "likes": [],
    "comments": []
  }
]
```

---

### ❌ `DELETE /posts/{post_id}`
Deletes a post if owned by the current user.

**Headers:**
```
X-User-ID: 1
```

**Response:**
```json
{
  "detail": "Post deleted"
}
```

---

## ❤️ Like & 💬 Comment Endpoints

### ❤️ `POST /like`
Simulates liking a post.

**Headers:**
```
X-User-ID: 2
```

**Body:**
```json
{
  "post_id": "uuid"
}
```

**Response:**
```json
{
  "detail": "User 2 liked post uuid"
}
```

---

### 💬 `POST /comment`
Simulates commenting on a post.

**Headers:**
```
X-User-ID: 2
```

**Body:**
```json
{
  "post_id": "uuid",
  "text": "Nice post!"
}
```

**Response:**
```json
{
  "detail": "User 2 commented on post uuid: Nice post!"
}
```

---

## 🧪 Sample Users
Use these IDs in the `X-User-ID` header:

- `1`: john_doe  
- `2`: jane_doe

---

## 🌐 Live Demo
Test the API interactively via Swagger UI:  
🔗 [InstaClone API – Swagger Docs](https://insta-clone-api-eyqn.onrender.com/docs)

Use `X-User-ID` header to simulate authentication.

---

## 🛠 Tech Stack
- FastAPI  
- Pydantic  
- Uvicorn  
- Python 3.10+

---

## 🧪 Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 📁 File Structure

```
insta_clone_api/
├── main.py
├── requirements.txt
├── database.py
├── dependencies.py
├── schemas.py
├── LICENSE
└── routers/
    └── posts.py
```

---

## 📜 License
This project is licensed under the [MIT License](https://github.com/nikhxxt/insta_clone_api/blob/main/LICENSE).
```

---

