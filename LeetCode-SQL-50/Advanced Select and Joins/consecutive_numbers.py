import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.sort_values(by = 'id')
    return logs[(logs.num == logs.shift(1).num) & (logs.num == logs.shift(2).num) & (logs.id == logs.shift(1).id + 1) & (logs.id == logs.shift(2).id + 2)].rename(columns = {'num':'ConsecutiveNums'})[['ConsecutiveNums']].drop_duplicates()