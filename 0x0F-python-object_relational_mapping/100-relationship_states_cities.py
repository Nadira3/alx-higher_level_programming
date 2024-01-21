#!/usr/bin/python3

# Write a script 14-model_city_fetch_by_state.py that
#    prints all City objects from the database hbtn_0e_14_usa:
#
#    Your script should take 3 arguments:
#        - mysql username, mysql password and database name
#    You must use the module SQLAlchemy
#    You must import State and Base from model_state -
#        from model_state import Base, State
#    Script should connect to a MySQL server running on localhost@3306
#    Results must be sorted in ascending order by cities.id
#    Results must be display as they are in the example below
#        (<state name>: (<city id>) <city name>)
#    Your code should not be executed when imported


""" Start link class to table in database """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='California')

    # Step x: Add the State instance and City instances to the session
    session.add(new_state)
    session.commit()  # Commit the State first to get its ID

    # Step x: Create instances of the City class
    new_city = City(name='San Francisco', state_id=new_state.id)

    # Set the state attribute for each City instance
    new_state.cities = new_city

    session.add(new_city)

    # Step x: Commit the changes to persist them in the database
    session.commit()
    session.close()
