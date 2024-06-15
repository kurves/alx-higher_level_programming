-- script to create cities by states

SELECT cities.id, cities.name, states.name  FROM states LEFT JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
