import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(prices,units_sold,how = 'outer', on = 'product_id')
    return df[(df.units.isna()) | ((df.start_date <= df.purchase_date) & (df.end_date >= df.purchase_date))].fillna(0).groupby('product_id').apply(lambda g,x,y: (sum(g[x]*g[y])/sum(g[y])).round(2),x = 'price', y = 'units').reset_index().rename(columns = {0:'average_price'}).fillna(0)