-- script to remove records:

DB_NAME="$1"

SQL_QUERY="DELETE FROM ${DB_NAME}.second_table WHERE score <= 5;"

mysql -e "$SQL_QUERY"
