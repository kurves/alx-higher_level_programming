-- script to record all scores


SQL_QUERY="SELECT score, name FROM ${DB_NAME}.second_table WHERE score >= 10 ORDER BY score DESC;"

mysql -e "$SQL_QUERY"
