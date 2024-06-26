#!/usr/bin/python3
"""This is the city class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """City class definition"""

    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes city's object instance"""
        super().__init__(*args, **kwargs)
