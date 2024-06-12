# Write your MySQL query statement below
SELECT ROUND(SUM(player_cond)/COUNT(DISTINCT player_id),2) AS fraction FROM (SELECT player_id,
IF(DATEDIFF(event_date ,LAG(event_date) OVER(partition by player_id ORDER BY event_date))= 1 AND
ROW_NUMBER() over(partition by player_id order by event_date) = 2,
1,0) as player_cond
FROM Activity) AS table1