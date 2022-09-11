#!/usr/bin/python3

"""
a script that lists all State objects, and corresponding City objects, contained in the database
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

    row = session.query(State).all()

    for state in row:
        print("{}: {}".format(state.id, state.name))
        for city in state.id:
            print("{}: {}".format(city.id, city.name))
    session.close()