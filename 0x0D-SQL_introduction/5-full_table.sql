

database_name=$1
table_name=$2

mysql -u root -p -e "USE $database_name; SHOW COLUMNS FROM $table_name;"
