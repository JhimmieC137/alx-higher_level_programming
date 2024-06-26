#!/usr/bin/python3
"""
    Start link class to table in database
"""
import sys
from relationship_state import Base
from relationship_city import City
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

    cities = db.query(City).options(joinedload(City.state)).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
