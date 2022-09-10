#!/usr/bin/python3
"""a python file that contains the class definition of a State and an instance Base = declarative_base()"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine, Column, Integer, String)

import MySQLdb
from sys import argv

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Base = declarative_base()


class State(Base):
    """Class State"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
