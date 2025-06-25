#!/usr/bin/python3
"""
This module delete all states contaning letter a
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)

    with Session() as session:
        to_delete = session.query(State).filter(State.name.like("%a%")).all()
        for state in to_delete:
            session.delete(state)
        session.commit()
