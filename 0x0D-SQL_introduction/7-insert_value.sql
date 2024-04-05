#!/bin/bash

# Usage: ./script_name database_name

database_name=$1

mysql -u root -p -e "USE $database_name; INSERT INTO first_table (id, name) VALUES (89, 'Best School');"
