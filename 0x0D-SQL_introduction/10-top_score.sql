#!/bin/bash

# Usage: ./script_name database_name

database_name=$1

mysql -u root -p $database_name << EOF
SELECT score, name FROM second_table ORDER BY score DESC;
EOF
