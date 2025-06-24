-- Lists ALL the cities of California that can be found IN the DATABASE
SELECT
    id,
    name
FROM
    cities
WHERE
    name = (
        SELECT
            id
        FROM
            states
        WHERE
            name = 'California'
    )
ORDER BY
    id ASC;