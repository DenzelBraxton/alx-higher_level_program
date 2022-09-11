#!/usr/bin/python3
"""
city class
"""

import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """Representation of a city"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state_id"))
