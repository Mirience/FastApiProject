from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    date_joined: datetime

class Category(BaseModel):
    id: int
    title: str
    description: str
    slug: str
    is_published: bool
    created_at: datetime

class Location(BaseModel):
    id: int
    name: str
    is_published: bool
    created_at: datetime

class Post(BaseModel):
    id: int
    title: str
    text: str
    pub_date: datetime
    is_published: bool
    created_at: datetime
    author_id: int
    location_id: Optional[int] = None
    category_id: Optional[int] = None
    image: Optional[str] = None

class Comment(BaseModel):
    id: int
    text: str
    created_at: datetime
    author_id: int
    post_id: int