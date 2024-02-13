-- Retrieve all records >10 from second table.
-- Then sort in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
