#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
        )
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).all()

    for i in rows:
        print("{}: {}".format(i.__dict__['id'], i.__dict__['name']))

    session.close()

    session.close()
