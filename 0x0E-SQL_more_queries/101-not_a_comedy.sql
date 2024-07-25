-- script to find show 

SELECT @comedy_genre_id := id
FROM tv_genres
WHERE name = 'Comedy';

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
