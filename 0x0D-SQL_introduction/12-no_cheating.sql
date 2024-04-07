#!/bin/bash

--script to records list

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

DB_NAME="$1"

SQL_QUERY="UPDATE ${DB_NAME}.second_table SET score = 10 WHERE name = 'Bob';"

mysql -e "$SQL_QUERY"
