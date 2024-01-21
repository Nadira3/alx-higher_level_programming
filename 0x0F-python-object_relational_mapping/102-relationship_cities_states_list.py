#!/usr/bin/python3

#   lists all City objects from the database hbtn_0e_101_usa

""" lists all City objects models """
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

    # for city, state in session.query(City, State).\
      #      filter(City.state_id == State.id).order_by(City.id).all():
       # print(f"{city.id}: {city.name} -> {state.name}")

    # Using the state relationship
    for city in session.query(City).all():
        print(f'{city.id}: {city.name} -> {city.state.name}')
    session.close()
