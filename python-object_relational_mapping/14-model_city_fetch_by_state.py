#!/usr/bin/python3
"""
This module is script that allow to print desired
element from two table
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    """
    This script that allow to print desired
    element from two tables
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)

    with Session() as session:
        rows = session.query(
            State, City).filter(
                City.state_id == State.id).order_by(
                    City.id).all()
        for state, city in rows:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
