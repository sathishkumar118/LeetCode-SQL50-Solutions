SELECT query_name,
round(avg(rating/position),2) as quality,
round(AVG(IF(rating < 3, 1, 0))*100,2) as poor_query_percentage
FROM Queries
GROUP BY query_name
HAVING query_name is not null