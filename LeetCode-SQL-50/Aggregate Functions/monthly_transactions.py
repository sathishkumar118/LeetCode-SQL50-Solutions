import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions.trans_date.dt.strftime('%Y-%m')
    transactions['country'] = transactions.country.fillna('null')
    transactions['approved_amount'] = np.where(transactions.state == 'approved', transactions.amount, None)
    return transactions.groupby(['month','country'], as_index = False).agg(
        trans_count = ('amount', 'count'),
        approved_count = ('approved_amount', 'count'),
        trans_total_amount = ('amount', 'sum'),
        approved_total_amount = ('approved_amount', 'sum')
    ).replace('null',nan)