#!/usr/bin/python3
"""
This module create a class state to link to the my sql table
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Define an object called state to link at table states"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)

    name =  Column(String(128), nullable=False)
