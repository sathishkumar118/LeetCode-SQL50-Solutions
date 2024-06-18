select category, count(account_id) - 1 as accounts_count
from
(
    select account_id,
    CASE 
        WHEN income < 20000 THEN 'Low Salary'
        WHEN income > 50000 THEN 'High Salary'
        ELSE 'Average Salary'
    END as category
    from Accounts
    union
    select -1 as account_id, 'Low Salary' as category
    union
    select -1 as account_id, 'High Salary' as category
    union
    select -1 as account_id, 'Average Salary' as category) as acc
group by category