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

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
