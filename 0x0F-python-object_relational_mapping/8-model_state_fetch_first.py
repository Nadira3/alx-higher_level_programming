#!/usr/bin/python3

# Write a script that prints the first State object
#    from the database hbtn_0e_6_usa
#
#    Your script should take 3 arguments:
#        - mysql username, mysql password and database name
#    You must use the module SQLAlchemy
#    You must import State and Bas
#    Script should connect to a MySQL server running on localhost@3306
#    The state you display must be the first in states.id
#    You are not allowed to fetch all states
#        from the database before displaying the result
#    The results must be displayed as they are in the example below
#    If the table states is empty, print Nothing followed by a new line
#    Your code should not be executed when imported


"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    session.close()
