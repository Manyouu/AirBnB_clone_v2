#!/usr/bin/python3
"""Module: `AirBnB/models/amenity.py`"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents Amenity class for MySQL database.

    Inherits from SQLAlchemy Base & links to MySQL amenities table.

    Attributes:
        __tablename__ (str): name of MySQL table for storing Amenities.
        name (sqlalchemy String): amenity's name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
                                    "Place",
                                    secondary="place_amenity",
                                    viewonly=False
                                    )
