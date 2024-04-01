#!/bin/bash

# Check if the database name is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

# Store the database name passed as argument
database_name="$1"
