-- script to show data
SELECT
    tv_shows.title,
    SUM(tv_show_ratings.rating) AS rating_sum
FROM
    tv_shows
