import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by = 'recordDate', inplace = True)
    res = pd.merge(weather.shift(1),weather,left_index = True, right_index = True, suffixes = ("_prev", ""))
    return res[(res.temperature_prev < res.temperature) & ((res.recordDate - res.recordDate_prev).dt.days == 1)][['id']]