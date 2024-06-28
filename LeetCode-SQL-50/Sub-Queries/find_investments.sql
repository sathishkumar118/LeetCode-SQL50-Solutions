select
round(sum(tiv_2016),2) as tiv_2016
from Insurance as i
left join
(
    select lat,lon from Insurance
    group by lat, lon
    having count(*) = 1
) as t1
on i.lat = t1.lat
and i.lon = t1.lon
left join
(
    select tiv_2015 from Insurance group by tiv_2015 having count(*) > 1
) as t2
on i.tiv_2015 = t2.tiv_2015
where
t1.lat is not null
and t1.lon is not null
and t2.tiv_2015 is not null