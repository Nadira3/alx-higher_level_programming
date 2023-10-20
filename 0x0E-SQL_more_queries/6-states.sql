-- creates the database hbtn_0d_usa and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- creates a table in a database
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
