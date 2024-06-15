SELECT p.product_id,IFNULL(ROUND(SUM(us.units*p.price)/SUM(us.units),2),0) as average_price FROM UnitsSold as us RIGHT JOIN Prices as p
on us.product_id = p.product_id and us.purchase_date >= p.start_date and us.purchase_date <= p.end_date
group by p.product_id