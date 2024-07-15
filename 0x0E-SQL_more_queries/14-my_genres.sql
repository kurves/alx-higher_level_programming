-- script to join tables


SELECT tv_genres.name AS genre
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
SELECT tv_genres.name
FROM  tv_shows
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
