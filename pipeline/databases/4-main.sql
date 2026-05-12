-- Create table and insert data


--
CREATE TABLE IF NOT EXISTS db_0.second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO db_0.second_table (id, name, score) VALUES (1, "Bob", 14);
INSERT INTO db_0.second_table (id, name, score) VALUES (2, "Roy", 5);
INSERT INTO db_0.second_table (id, name, score) VALUES (3, "John", 10);
INSERT INTO db_0.second_table (id, name, score) VALUES (4, "Bryan", 8);



select * from db_0.second_table;

delete from db_0.second_table;