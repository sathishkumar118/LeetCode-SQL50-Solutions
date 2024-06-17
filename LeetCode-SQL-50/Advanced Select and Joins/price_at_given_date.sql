SELECT product_id, new_price as price
FROM
(
    SELECT *,
    ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) as row_num
    FROM Products
    WHERE change_date <= '2019-08-16'
    ) as p
WHERE row_num = 1
UNION
SELECT DISTINCT product_id, 10 as price
FROM Products
WHERE product_id not in
(
    SELECT product_id from Products
    WHERE change_date <= '2019-08-16'
)