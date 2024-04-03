#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

# Extract the database name from the command-line argument
database_name="$1"


sql_query="CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);"

# Run the SQL query to create the table
mysql -u your_username -p your_password -e "USE $database_name; $sql_query"
