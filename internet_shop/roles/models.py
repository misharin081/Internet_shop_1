from django.db import models
from sqlalchemy import Column, Integer, String
from database import Base


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    role_name = Column(String(10), nullable=False)
