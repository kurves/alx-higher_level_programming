-- script to find show 

SELECT @comedy_genre_id := id
FROM tv_genres
WHERE name = 'Comedy';

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
	SELECT tv_show_genres.show_id
    FROM tv_show_genres
    WHERE tv_show_genres.genre_id = @comedy_genre_id
)
ORDER BY tv_shows.title ASC;
