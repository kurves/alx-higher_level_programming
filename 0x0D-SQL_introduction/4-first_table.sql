-- create table
-- script to list databases

database_name="$1"

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

