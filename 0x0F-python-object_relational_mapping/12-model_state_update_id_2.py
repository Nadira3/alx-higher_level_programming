#!/usr/bin/python3

# Write a script that changes the name of a State object from the database hbtn_0e_6_usa
#
#    Your script should take 3 arguments: mysql username, mysql password and database name
#    You must use the module SQLAlchemy
#    You must import State and Base from model_state - from model_state import Base, State
#    Your script should connect to a MySQL server running on localhost at port 3306
#    Change the name of the State where id = 2 to New Mexico
#    Your code should not be executed when imported

""" module that updates an object """

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    # find the object
    state = session.query(State).filter_by(id=2).one()
    # update the object
    state.name = "New Mexico"
    # commit your changes
    session.commit()
   
    # close the session
    session.close()
