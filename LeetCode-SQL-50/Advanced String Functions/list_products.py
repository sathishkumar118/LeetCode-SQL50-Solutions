import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df_filter = (orders.order_date.dt.year == 2020) & (orders.order_date.dt.month == 2)
    pdts_gp = orders.loc[df_filter].groupby('product_id').unit.sum().reset_index()
    return pdts_gp[pdts_gp.unit >= 100].merge(products, on = 'product_id', how = 'left')[['product_name','unit']]