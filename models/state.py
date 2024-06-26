#!/usr/bin/python3
"""Defines the State class."""

import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents state class of MySQL database.

    Inherits from SQLAlchemy Base & links to MySQL table states.

    Attributes:
        __tablename__ (str): name of MySQL table for storing States.
        name (sqlalchemy String): name of the State.
        cities (sqlalchemy-relationship): State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Retrieve list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
