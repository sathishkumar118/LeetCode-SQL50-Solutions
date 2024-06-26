import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    cust_grp = customer.sort_values(by = 'visited_on').groupby(by = 'visited_on', as_index = False).amount.sum()
    cust_grp['average_amount'] = cust_grp.rolling(7).amount.mean().round(2)
    cust_grp['amount'] = cust_grp.rolling(7).amount.sum()
    return cust_grp[cust_grp.amount.notna()]