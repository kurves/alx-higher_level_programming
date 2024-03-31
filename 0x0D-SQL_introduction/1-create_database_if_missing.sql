#!/bin/bash

# Prompt the user for MySQL credentials
read -p "Enter MySQL username: " username
read -sp "Enter MySQL password: " password

# Use the mysql command to connect to the server and create the database
mysql -u "$username" -p"$password" -e "CREATE DATABASE IF NOT EXISTS hbtn_0c_0;"
