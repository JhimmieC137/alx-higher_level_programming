#!/usr/bin/python3
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import declarative_base

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
            )
    )

    Base = declarative_base()
    Base.metadata.create_all(engine)

    class State(Base):
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
