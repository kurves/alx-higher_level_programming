-- create table
-- script to list databases

database_name="$1"


sql_query="CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);"

mysql -u your_username -p your_password -e "USE $database_name; $sql_query"
