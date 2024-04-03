#!/bin/bash

-- script to list databases

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

database_name="$1"


sql_query="CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);"

mysql -u your_username -p your_password -e "USE $database_name; $sql_query"
