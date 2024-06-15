import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    gp = my_numbers.value_counts()
    return pd.DataFrame({'num' : [gp[gp == 1].reset_index().num.max()]})
