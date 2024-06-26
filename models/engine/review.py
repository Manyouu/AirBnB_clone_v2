#!/usr/bin/python3
"""Defines the Review class."""

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represents a review objects for MySQL database.

    Inherits from SQLAlchemy Base & links the MySQL table review objects..

    Attributes:
        __tablename__ (str): name of the MySQL table to store Reviews.
        text (sqlalchemy String): review class' description.
        place_id (sqlalchemy String): review class' place id.
        user_id (sqlalchemy String): review class' user id.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
