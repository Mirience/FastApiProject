from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # В реальном проекте храним хеш
    is_active = Column(Boolean, default=True)
    date_joined = Column(DateTime(timezone=True), server_default=func.now())
    
    # Связи
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False, verbose_name="Заголовок")
    description = Column(Text, nullable=False, verbose_name="Описание")
    slug = Column(String, unique=True, index=True, nullable=False)
    is_published = Column(Boolean, default=True, verbose_name="Опубликовано")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), verbose_name="Добавлено")
    
    # Связи
    posts = relationship("Post", back_populates="category")


class Location(Base):
    __tablename__ = "locations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False, verbose_name="Название места")
    is_published = Column(Boolean, default=True, verbose_name="Опубликовано")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), verbose_name="Добавлено")
    
    # Связи
    posts = relationship("Post", back_populates="location")


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False, verbose_name="Заголовок")
    text = Column(Text, nullable=False, verbose_name="Текст")
    pub_date = Column(DateTime(timezone=True), default=datetime.now, nullable=False, 
                     verbose_name="Дата и время публикации")
    is_published = Column(Boolean, default=True, verbose_name="Опубликовано")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), verbose_name="Добавлено")
    
    # Внешние ключи
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    
    # Поле для изображения (храним путь к файлу)
    image = Column(String, nullable=True, verbose_name="Изображение")
    
    # Связи
    author = relationship("User", back_populates="posts")
    location = relationship("Location", back_populates="posts")
    category = relationship("Category", back_populates="posts")
    comments = relationship("Comment", back_populates="post", order_by="Comment.created_at")


class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False, verbose_name="Текст комментария")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), verbose_name="Дата")
    
    # Внешние ключи
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    
    # Связи
    author = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")