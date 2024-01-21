#!/usr/bin/python3

# Write a Python file similar to model_state.py named
#    model_city.py that contains the class definition of a City.
#
#    City class:
#        inherits from Base (imported from model_state)
#        links to the MySQL table cities
#    class attribute id that represents a column of an auto-generated,
#        unique integer, can’t be null and is a primary key
#    class attribute name that represents a
#        column of a string of 128 characters and can’t be null
#    class attribute state_id that represents a column of an integer,
#        can’t be null and is a foreign key to states.id
#    You must use the module SQLAlchemy

"""
    module that contains the class definition of a State
    and an instance Base = declarative_base()
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """ City class definition """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
