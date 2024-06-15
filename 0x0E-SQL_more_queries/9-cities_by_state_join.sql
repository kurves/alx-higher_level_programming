-- script to create cities by states

SELECT cities.id, cities.name, states.name  FROM states LEFT JOIN states ON states.id = cities.state_id  ORDER BY cities.id ASC;
