#!/usr/bin/python3

# Write a script that takes in the name of a state as an argument
# and lists all cities of that state, using the database hbtn_0e_4_usa
#
#    Your script should take 4 arguments:
#        - mysql username,
#        - mysql password, database name and
#        - state name (SQL injection free!)
#    You must use the module MySQLdb (import MySQLdb)
#    Script should connect to MySQL server running on localhost at port 3306
#    Results must be sorted in ascending order by cities.id
#    You can use only execute() once
#    The results must be displayed as they are in the example below
#    Your code should not be executed when imported

"""
    a module that lists all cities from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    argv = sys.argv
    if len(argv) == 5:
        conn = MySQLdb.connect(
                host="localhost", port=3306, user=argv[1],
                passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute('''SELECT cities.name FROM cities
                    JOIN states ON cities.state_id=states.id
                    WHERE states.name=%s''', (argv[4], ))
        query_rows = cur.fetchall()
        rows = list(row[0] for row in query_rows)
        print(*rows, sep=", ")
        cur.close()
        conn.close()
