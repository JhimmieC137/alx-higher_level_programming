#!/usr/bin/python3

"""
    Start link class to table in database
"""
import sys
from model_city import Base, City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import joinedload, sessionmaker


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

    list_of_cities = db().query(City)\
        .options(joinedload(City.state))\
        .order_by(City.id.asc())\
        .all()
    for city in list_of_cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
