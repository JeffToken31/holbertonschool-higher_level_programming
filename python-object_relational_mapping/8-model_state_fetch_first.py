#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)

    with Session() as session:
        row = session.query(State).order_by(State.id).first()
        if not row:
            print("Nothing")
        print("{}: {}".format(row.id, row.name))
