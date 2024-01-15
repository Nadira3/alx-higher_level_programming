#!/usr/bin/python3

# Write a python file that contains the class definition of a State
#   and an instance Base = declarative_base():
#
#    State class:
#        inherits from Base Tips
#        links to the MySQL table states
#    class attribute id that represents a column of an auto-generated
#        unique integer, can’t be null and is a primary key
#    class attribute name that represents a column of a string
#        with maximum 128 characters and can’t be null
#    You must use the module SQLAlchemy

""" module that defines Base and State """
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    """ State class definition """
    __tablename__ = 'states'
    ...
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))

    cities = relationship("City", back_populates="state")
