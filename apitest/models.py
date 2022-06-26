from sqlalchemy.orm import relationship
from core.db import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from user.models import User

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(length=350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship(User)