-- script to create cities by states

SELECT cities.id, cities.name, (
    SELECT states.name FROM states WHERE states.id = cities.state_id
) AS state_name
FROM cities
ORDER BY cities.id ASC;

SELECT cities.id, cities.name, states.name AS state_name FROM states JOIN cities.id  ON cities.state_id = states.id ORDER BY cities.id ASC;
