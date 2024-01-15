#!/usr/bin/python3

# Write a script that adds the State object
#        “Louisiana” to the database hbtn_0e_6_usa
#
#    Your script should take 3 arguments:
#        - mysql username, mysql password and database name
#    You must use the module SQLAlchemy
#    You must import State and Base from model_state
#        - from model_state import Base, State
#    Script should connect to a MySQL server running on localhost@3306
#    Print the new states.id after creation
#    Your code should not be executed when imported

""" module that imserts an object into a database """

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    session.add(State(name='Louisiana'))

    state = session.query(State).order_by(State.id).all()
    print(state[-1].id)

    session.commit()
    session.close()
