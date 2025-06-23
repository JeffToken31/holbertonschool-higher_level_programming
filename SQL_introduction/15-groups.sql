--lists the number of records WITH the same score IN the TABLE
SELECT
    score,
    COUNT(score) AS 'number'
FROM
    second_table
GROUP BY
    score
ORDER BY
    score DESC