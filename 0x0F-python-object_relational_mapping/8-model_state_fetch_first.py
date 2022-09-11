#!/usr/bin/python3
"""a script that prints the first State object from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id).first()
    if first is not None:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
