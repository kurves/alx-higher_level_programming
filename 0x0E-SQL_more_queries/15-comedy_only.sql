-- script to etch specific genre
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
SELECT
    g.name AS tv_genres_name
FROM
    tv_shows t
JOIN
    tv_show_genres tg ON t.id = tg.tv_show_id
JOIN
    genres g ON tg.genre_id = g.id
WHERE
    t.title = 'Dexter'
ORDER BY
    g.name ASC;
