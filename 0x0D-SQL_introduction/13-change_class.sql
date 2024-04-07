#!/bin/bash

-- script to remove records:
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

DB_NAME="$1"

SQL_QUERY="DELETE FROM ${DB_NAME}.second_table WHERE score <= 5;"

mysql -e "$SQL_QUERY"
