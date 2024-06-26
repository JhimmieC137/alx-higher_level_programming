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


Base = declarative_base()


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
