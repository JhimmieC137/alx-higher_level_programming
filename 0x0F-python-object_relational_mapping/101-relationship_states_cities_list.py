#!/usr/bin/python3
"""
    Start link class to table in database
"""
import sys
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, joinedload


if __name__ == "__main__":
    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost/{}'
                    .format(
                        sys.argv[1],
                        sys.argv[2],
                        sys.argv[3]
                    ),
                    pool_pre_ping=True
            )

    Base.metadata.create_all(engine)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session()

    states = db.query(State).options(joinedload(State.cities)).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
