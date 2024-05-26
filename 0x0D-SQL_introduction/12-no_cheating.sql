--script to records list


SQL_QUERY="UPDATE ${DB_NAME}.second_table SET score = 10 WHERE name = 'Bob';"

mysql -e "$SQL_QUERY"
