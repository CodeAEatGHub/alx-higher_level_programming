-- Lists all records in descending order with name and score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
