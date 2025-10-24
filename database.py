from uuid import UUID
from datetime import datetime

fake_posts_db: List[Dict[str, Any]] = [
    {
        "id": UUID("..."),  # use uuid4() when creating
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
