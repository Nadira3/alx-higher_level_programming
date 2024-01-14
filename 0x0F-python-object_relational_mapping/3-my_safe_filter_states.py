#!/usr/bin/python3

# Write a script that takes in an argument and displays
# all values in the states table of hbtn_0e_0_usa where
# name matches the argument.
#
#    Your script should take 4 arguments:
#    - mysql username, mysql password, database name and
#    - state name searched (no argument validation needed)
#    You must use the module MySQLdb (import MySQLdb)
#    Script connects to MySQL server running on localhost@3306
#    You must use format to create the SQL query with the user input
#    Results must be sorted in ascending order by states.id
#    Results must be displayed as they are in the example below
#    Your code should not be executed when imported

"""
    a module that lists all states starting
    from the database hbtn_0e_0_usa that matches
    the argument given

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
        cur.execute(
                '''SELECT * FROM states WHERE name LIKE BINARY %s
                ORDER BY id ASC''', (argv[4], ))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
