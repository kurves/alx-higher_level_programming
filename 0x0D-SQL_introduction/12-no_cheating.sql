#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

# Extract the database name from the command-line argument
DB_NAME="$1"

# Define the SQL query to update the score of Bob to 10
SQL_QUERY="UPDATE ${DB_NAME}.second_table SET score = 10 WHERE name = 'Bob';"

# Execute the SQL query using the mysql command
mysql -e "$SQL_QUERY"
