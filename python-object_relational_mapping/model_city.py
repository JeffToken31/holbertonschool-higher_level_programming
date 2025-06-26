#!/usr/bin/python3
"""
This module create a class state to link to the my sql table
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()


class City(Base):
    """Define an object called City to link at table Cities"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
