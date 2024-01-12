## Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).


Without ORM:
```\
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
    - Why Python programming is awesome
    - How to connect to a MySQL database from a Python script
    - How to SELECT rows in a MySQL table from a Python script
    - How to INSERT rows in a MySQL table from a Python script
    - What ORM means
    - How to map a Python Class to a MySQL table
    - How to create a Python Virtual Environment

Copyright © 2024 ALX, All rights reserved.
