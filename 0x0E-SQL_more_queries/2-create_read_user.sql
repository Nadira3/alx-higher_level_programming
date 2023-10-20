-- creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates the MySQL server user user_0d_2
-- user_0d_2 password should be set to user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- user_0d_2 should have select privileges
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
