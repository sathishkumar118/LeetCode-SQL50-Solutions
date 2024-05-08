select id, sum(num) as num from
(
  select * from
  (
    select requester_id as id, count(distinct accepter_id) as num
    from
    RequestAccepted
    group by requester_id
  ) as req
  union all
  select * from
  (
    select accepter_id as id, count(distinct requester_id) as num
    from
    RequestAccepted
    group by accepter_id
  ) as acc
) as tab
group by id
order by num desc
limit 1