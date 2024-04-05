#!/bin/bash

-- script to insert row
-- insert name and id
database_name=$1

mysql -u root -p -e "USE $database_name; INSERT INTO first_table (id, name) VALUES (89, 'Best School');"
