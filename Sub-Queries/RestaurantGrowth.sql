select
  visited_on,
  min(7_day_total) as amount,
  round(min(7_day_total)/7,2) as average_amount
from
(
  select
    visited_on,
    sum(amount)
    OVER(ORDER BY visited_on
    range BETWEEN interval 6 day PRECEDING AND CURRENT ROW)
    as 7_day_total
  from
  Customer
) as c1
where
  visited_on >=
  (
    select DATE_ADD(min(visited_on), INTERVAL 6 DAY) as min_date
    from Customer
  )
group by visited_on