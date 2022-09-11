#!/usr/bin/python3
"""
prints all City objects from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                        argv[2],
                                                                        argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(City, State).filter(City.state_id == State.id)\
                                            .order_by(City.id).all()
    for city, state in row:
        print("{}: ({}) ({}".format(state.name, city.id, city.name))
    session.close()
