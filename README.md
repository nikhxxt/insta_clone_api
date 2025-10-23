
# 📸 InstaClone API

A modular FastAPI backend simulating Instagram-style post activities. Built for clarity, authentication flow demonstration, and cloud deployment. Uses in-memory storage and header-based user simulation for simplicity and speed.




[![FastAPI](https://img.shields.io/badge/FastAPI-0.1.0-green)](https://fastapi.tiangolo.com/)
[![Render Deploy](https://img.shields.io/badge/Deploy-Render-blue)](https://render.com/)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/nikhxxt/insta_clone_api-/blob/main/LICENSE)


---

## 📚 Table of Contents

- [Features](#-features)  
- [Authentication Flow](#-authentication-flow)  
- [Post Endpoints](#-post-endpoints)  
- [Live Demo](#-live-demo)  
- [Why Header-Based Auth](#-why-header-based-auth)  
- [Tech Stack](#-tech-stack)  
- [Deployment](#-deployment)  
- [File Structure](#-file-structure)  
- [Sample Curl Commands](#-sample-curl-commands)  
- [License](#-license)  

---

## 🚀 Features

✅ Header-based user authentication (`X-User-ID`)  
📝 Create, view, and delete posts  
🔐 Ownership checks for delete operations  
💬 Simulated like and comment endpoints  
📦 Modular structure with FastAPI routers and dependencies  
🧪 In-memory DB for quick prototyping  

---

## 📬 Authentication Flow

All protected endpoints require a valid `X-User-ID` header.

**Example:**

```
X-User-ID: 1
```

If the user ID is not found in `fake_users_db`, the API returns a 404 error.

---

## 📝 Post Endpoints

### ➕ POST `/posts/`  
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
  "id": 1,
  "text": "Hello from InstaClone!",
  "owner_id": 1
}
```

---

### 📄 GET `/posts/`  
Returns all posts.

---

### ❌ DELETE `/posts/{post_id}`  
Deletes a post if owned by the current user.

**Headers:**
```
X-User-ID: 1
```

---

### ❤️ POST `/like`  
Simulates liking a post.

**Body:**
```json
{
  "post_id": 1,
  "user_id": 2
}
```

---

### 💬 POST `/comment`  
Simulates commenting on a post.

**Body:**
```json
{
  "post_id": 1,
  "user_id": 2,
  "text": "Nice post!"
}
```

---

## 🌐 Live Demo

Test the API interactively via Swagger UI:

🔗 [InstaClone API – Swagger Docs](https://insta-clone-api-eyqn.onrender.com/docs)

Use `X-User-ID` header to simulate authentication.

---

## 🔐 Why Header-Based Auth?

- 🔄 Stateless and simple  
- 🧪 Ideal for mock APIs and demos  
- 🚀 Fast to deploy and test  
- 🧩 Easily extendable to JWT or OAuth  

---

## 🛠 Tech Stack

- FastAPI  
- Pydantic  
- Uvicorn  
- Python 3.10+  

---

## 🌐 Deployment

**Render Setup**

- **Build Command:**
  ```bash
  pip install -r requirements.txt
  ```

- **Start Command:**
  ```bash
  uvicorn main:app --host 0.0.0.0 --port $PORT
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
└── routers/
    └── posts.py
```

---

## 🧪 Sample Curl Commands

### ➕ Create Post

```bash
curl -X POST https://your-app-url.onrender.com/posts/ \
  -H "X-User-ID: 1" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello from InstaClone!"}'
```

### ❌ Delete Post

```bash
curl -X DELETE https://your-app-url.onrender.com/posts/1 \
  -H "X-User-ID: 1"
```

---

📜 License
This project is licensed under the MIT License.
