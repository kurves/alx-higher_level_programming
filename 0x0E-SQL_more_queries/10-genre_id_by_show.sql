-- script to join tables

SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
  JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
  JOIN $DB_NAME.genres g ON tg.genre_id = g.id
  ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
