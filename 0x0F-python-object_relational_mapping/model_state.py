#!/usr/bin/python3
"""
    This script creates the model
    State
"""
import sys
from sqlalchemy import (create_engine, Column, Integer, String)
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


class State(Base):
    """
        The state model with attributes
    """
    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
        )
    name = Column(
        String(128),
        nullable=False
        )
