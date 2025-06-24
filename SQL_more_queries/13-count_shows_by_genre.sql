-- List all genres AND displays the number of shows linked TO each.
SELECT
    tv_genres.name,
    count(tv_show_genres.genre_id) AS number_of_shows
FROM
    tv_genres
    INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY
    tv_genres.name
ORDER BY
    number_of_shows DESC;