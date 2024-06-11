# Write your MySQL query statement below
SELECT ROUND(AVG(orderType)*100,2) AS immediate_percentage FROM (SELECT customer_id,IF(order_date = customer_pref_delivery_date,1,0) as orderType,
ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS orderNum
FROM Delivery) as tab1
WHERE orderNum = 1