-- updates the score of Bob to 10 in the table second_table
-- using the name field
-- lists all records of the table second_table of the database hbtn_0c_0
UPDATE second_table SET score=10 WHERE name="Bob" ORDER BY score DESC
