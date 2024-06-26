#!/usr/bin/python3
"""
    This script creates the model
    state and binds it to the database
    engine
"""
import sys
from sqlalchemy import (MetaData, Table,
                        create_engine, Column, Integer, String)
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'
    .format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        )
    )
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.metadata.create_all(engine)
metadata = MetaData()

State = Table(
            "states",
            metadata,
            Column(
                    'id',
                    Integer,
                    primary_key=True,
                    autoincrement=True,
                    nullable=False
            ),
            Column(
                    'name',
                    String(128),
                    nullable=False
            )
        )
