-- Lists the number of records with the same score along with the score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
