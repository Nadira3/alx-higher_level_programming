# MySql Introduction

 contains a script that:

    - [lists all databases of your MySQL server]

    - [creates the database hbtn_0c_0 in your MySQL server]

    - [deletes the database hbtn_0c_0 in your MySQL server]

    - [lists all the tables of a database in your MySQL server]
        - `The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)`

    - [creates a table called first_table in the current database in your MySQL server]
        - `first_table description:
                id INT
                name VARCHAR(256)`

    - [prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server]

    - [lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server]

    - [inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server]
        - `New row:
            id = 89
            name = Best School`

    - [displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server]

    - [creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows]
        - `second_table description:
            id INT
            name VARCHAR(256)
            score INT
            
            The database name will be passed as an argument to the mysql command
            If the table second_table already exists, the script does not fail`
        - `create these records:
            id = 1, name = “John”, score = 10
            id = 2, name = “Alex”, score = 3
            id = 3, name = “Bob”, score = 14
            id = 4, name = “George”, score = 8`

    - [lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server]
        - `Results are displayed both the score and the name (in this order)
            Records are ordered by score (top first)`
    
    - [lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server]
        - `Results are displayed both the score and the name (in this order)
            Records are ordered by score (top first)`
    
    - [updates the score of Bob to 10 in the table second_table]

    - [removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server]

    - [computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server]
        - `The result column name is average`

    - ["lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server]
        - `The result displays:
            the score
            the number of records for this score with the label number`
        - `The list is sorted by the number of records (descending)`

    - [lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server without rows]
