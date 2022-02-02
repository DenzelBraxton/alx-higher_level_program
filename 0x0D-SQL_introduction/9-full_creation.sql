-- script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
-- create new table
CREATE TABLE IF NOT EXISTS secound_table (id INT, name VARCHAR(256), score INT);

-- Add new record to the table
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(1, 'John', 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(2, 'Alex', 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(3, 'Bob', 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(4, 'George', 8);

