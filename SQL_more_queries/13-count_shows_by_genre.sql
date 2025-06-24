-- List all genres AND displays the number of shows linked TO each.
SELECT
    tv_genres.name,
    count(tv_show_genres.genre_id) AS number_of_shows
FROM
    tv_genres
    RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE
    tv_show_genres.genre_id IS NOT NULL
GROUP BY
    tv_genres.name
ORDER BY
    number_of_shows DESC;