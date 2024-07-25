-- Step 1: Find the ID of the genre titled "Comedy"
SELECT @comedy_genre_id := id
FROM tv_genres
WHERE name = 'Comedy';
