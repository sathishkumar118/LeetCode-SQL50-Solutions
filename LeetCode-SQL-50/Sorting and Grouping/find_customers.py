import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    gp = customer.groupby('customer_id', as_index = False).nunique()
    return gp[gp.product_key == len(product)][['customer_id']]