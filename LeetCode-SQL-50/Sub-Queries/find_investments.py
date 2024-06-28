import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'tiv_2016' : [insurance[insurance.pid.isin(insurance[insurance.duplicated(subset = ['tiv_2015'], keep = False)].pid) &
    insurance.pid.isin(insurance.drop_duplicates(subset = ['lat','lon'], keep = False).pid)].tiv_2016.sum()]})