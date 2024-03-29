#!/usr/bin/python3

# Write a script that lists all cities from the database hbtn_0e_4_usa
#
#    Your script should take 3 arguments:
#        - mysql username,
#        - mysql password and
#        - database name
#    You must use the module MySQLdb (import MySQLdb)
#    Script should connect to MySQL server
#        running on localhost at port 3306
#    Results must be sorted in ascending order by cities.id
#    You can use only execute() once
#    Results must be displayed as they are in the example below
#    Your code should not be executed when imported

"""
    a module that lists all cities from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    argv = sys.argv
    if len(argv) == 4:
        conn = MySQLdb.connect(
                host="localhost", port=3306, user=argv[1],
                passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute('''SELECT cities.id, cities.name, states.name
        FROM cities JOIN states
        ON cities.state_id=states.id ORDER BY cities.id ASC''')
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
