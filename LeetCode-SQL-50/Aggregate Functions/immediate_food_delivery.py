import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['is_immediate'] = delivery.order_date == delivery.customer_pref_delivery_date
    return pd.DataFrame({'immediate_percentage' : [delivery.sort_values(by = 'order_date').groupby('customer_id').first().reset_index().is_immediate.mean().round(4)*100]})