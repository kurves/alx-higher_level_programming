#!/bin/bash

-- script to record all scores

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

DB_NAME="$1"

SQL_QUERY="SELECT score, name FROM ${DB_NAME}.second_table WHERE score >= 10 ORDER BY score DESC;"

mysql -e "$SQL_QUERY"
