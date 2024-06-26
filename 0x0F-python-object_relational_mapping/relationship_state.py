#!/usr/bin/python3
"""
Module that contains the class definition of a State.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

meta = MetaData()
Base = declarative_base(metadata=meta)

class State(Base):
    """
    Class representing a state in the database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
