#!/usr/bin/python3
"""
    Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session()

    state = State(name='California')
    db.add(state)
    db.commit()
    db.refresh(state)

    city = City(name='San Francisco', state_id=state.id)
    db.add(city)
    db.commit()
    db.refresh(city)
