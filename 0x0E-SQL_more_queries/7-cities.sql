-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server 
-- create a database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa; 
-- use database 
USE hbtn_0d_usa 
-- create a table in the database 
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL AUTO_INCREMENT, 
state_id INT NOT NULL, 
name VARCHAR(255) NOT NULL, 
PRIMARY KEY(id), 
FOREIGN KEY(state_id) REFERENCES state(id));

