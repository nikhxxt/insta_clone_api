from typing import Dict, List, Any
from uuid import uuid4
from datetime import datetime

fake_users_db: Dict[int, Dict[str, str]] = {
    1: {"username": "john_doe"},
    2: {"username": "jane_doe"}
}

fake_posts_db: List[Dict[str, Any]] = [
    {
        "id": uuid4(),  # generates a valid UUID
        "text": "Hello world!",
        "owner_id": 1,
        "created_at": datetime.utcnow(),
        "likes": [],  # list of user_ids
        "comments": [  # list of comment dicts
            {
                "user_id": 2,
                "text": "Nice post!",
                "timestamp": datetime.utcnow()
            }
        ]
    }
]
