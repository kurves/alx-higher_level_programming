SELECT
    tv_shows.title,
    tv_genres.name
FROM
    tv_shows
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
