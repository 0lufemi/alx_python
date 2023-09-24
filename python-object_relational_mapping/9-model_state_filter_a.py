#!/usr/bin/python3
"""
script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
        )

    Base.metadata.create_all(engine)

    session = Session(engine)

    results = session.query(State).all()

    for result in results:
        if 'a' in result.__dict__['name']:
            print(f"{result.__dict__['id']}: {result.__dict__['name']}")

    session.close()
