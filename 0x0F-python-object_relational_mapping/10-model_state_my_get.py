#!/usr/bin/python3
"""
    Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


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
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    state_name = sys.argv[4]
    state = db().query(State).filter(State.name == state_name).first()
    if not state:
        print("Not found")
    else:
        print(state.id)
