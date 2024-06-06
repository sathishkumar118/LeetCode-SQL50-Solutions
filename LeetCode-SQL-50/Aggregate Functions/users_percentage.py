import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    return (register.groupby('contest_id').count()/len(users)*100).round(2).reset_index().rename(columns = {'user_id':'percentage'}).sort_values(by = ['percentage','contest_id'], ascending = [False, True])