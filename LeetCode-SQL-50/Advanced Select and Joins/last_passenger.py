import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values(by = 'turn')
    queue['cum_weight'] = queue.weight.cumsum()
    return queue[queue.cum_weight <= 1000].tail(1)[['person_name']]