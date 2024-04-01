#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

database_name="$1"


read -p "Enter MySQL username: " username
read -sp "Enter MySQL password: " password
echo

mysql -u "$username" -p"$password" -e "USE $database_name; SHOW TABLES;"
