#!/usr/bin/python3
"""
a script that prints the State object with the name 
passed as argument from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                        argv[2],
                                                                        argv[3]))
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(name=argv[4]).first()

    if states is not None:
        print(str(states.id))
    else:
        print("Not found")
    session.close()
    