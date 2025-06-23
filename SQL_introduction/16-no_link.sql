-- List all record with specific conditions
SELECT
    score,
    name
FROM
    second_table
WHERE
    name IS NOT NULL
ORDER BY
    score DESC