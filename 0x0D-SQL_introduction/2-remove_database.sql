#!/bin/bash

-- script to delete database
read -p "Enter MySQL username: " username
read -sp "Enter MySQL password: " password

mysql -u "$username" -p"$password" -e "DROP DATABASE IF EXISTS hbtn_0c_0;"
