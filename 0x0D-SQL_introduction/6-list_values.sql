
-- script to list values from tale

database_name=$1

mysql -u root -p -e "USE $database_name; SELECT * FROM first_table;"
