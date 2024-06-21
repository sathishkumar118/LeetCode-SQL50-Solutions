SELECT product_name,units as unit FROM Products as p
LEFT JOIN
(
    SELECT product_id, SUM(unit) as units
    FROM Orders
    WHERE
    MONTH(order_date) = 2
    AND YEAR(order_date) = 2020
    GROUP BY product_id) AS o
ON
p.product_id = o.product_id
WHERE units >= 100