import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    return activity[(activity.activity_date > '2019-06-27') & (activity.activity_date <= '2019-07-27')].groupby('activity_date').user_id.nunique().reset_index().rename(columns = {'activity_date':'day','user_id':'active_users'})