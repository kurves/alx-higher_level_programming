-- script to join tables

SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
  JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
  JOIN tv_show_genres  ON tv_show_genres.genre_id = genre.id
  GROUP BY tv_shows.title, tv_show_genres.genre_id
  ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
