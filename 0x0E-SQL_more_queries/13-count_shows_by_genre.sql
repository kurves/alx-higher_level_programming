-- script to join tables

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
