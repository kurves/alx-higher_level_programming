!/bin/bash

-- script to no of records

database_name=$1

mysql -u root -p -e "USE $database_name; SELECT COUNT(*) FROM first_table WHERE id = 89;"