import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(visits, transactions, how = 'left', left_on = 'visit_id', right_on = 'visit_id')
    return res[res.transaction_id.isnull()].groupby('customer_id').count().visit_id.rename('count_no_trans').reset_index()