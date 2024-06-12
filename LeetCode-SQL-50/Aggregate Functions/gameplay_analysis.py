import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values('event_date')
    gp_df = activity.groupby('player_id').nth(0).merge(activity.groupby('player_id').nth(1), on = 'player_id', how = 'left')
    return pd.DataFrame({'fraction':[((gp_df.event_date_y - gp_df.event_date_x).dt.days == 1).mean().round(2)]})