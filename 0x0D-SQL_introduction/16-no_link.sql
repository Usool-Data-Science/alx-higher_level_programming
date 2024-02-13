-- Retrieve rows with name value.
-- Sort them in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
