#!/usr/bin/python3

"""
    This script creates the model
    city and binds it to the database
    engine
"""

import sys
from sqlalchemy import (MetaData, Table, ForeignKey,
                        create_engine, Column, Integer, String)
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

from relationship_state import Base


class City(Base):
    """
        The city model with attributes
    """
    __tablename__ = "cities"
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
    state_id = Column(
            Integer,
            ForeignKey("states.id", ondelete="CASCADE"),
            nullable=True
            )
    state = relationship(
            "State",
            back_populates="cities",
            uselist=False
            )
