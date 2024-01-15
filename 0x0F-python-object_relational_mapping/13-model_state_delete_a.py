#!/usr/bin/python3

# Write a script that deletes all State objects with a name
#        containing the letter a from the database hbtn_0e_6_usa
#    Your script should take 3 arguments:
#        - mysql username, mysql password and database name
#    You must use the module SQLAlchemy
#    You must import State and Base from model_state
#        - from model_state import Base, State
#    Script should connect to a MySQL server running on localhost@3306
#    Results must be sorted in ascending order by states.id
#    The results must be displayed as they are in the example below
#    Your code should not be executed when imported

"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    #connext and create a session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    #find the matching objects and delete
    for state in session.query(State).order_by(State.id).filter(State.name.like('%a%')).all(): 
        session.delete(state)

    # commit the changes
    session.commit()
    session.close()
