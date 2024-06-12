-- script to create cities by states

SELECT cities.id, cities.name, states.name AS state_name FROM states JOIN cities.id  ON cities.state_id = states.id ORDER BY cities.id ASC;
