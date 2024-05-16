import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    res = activity[activity.activity_type == 'start'].set_index(['machine_id','process_id']).join(activity[activity.activity_type == 'end'].set_index(['machine_id','process_id']), rsuffix = '_end')
    res['processing_time'] = res.timestamp_end - res.timestamp
    print(res['processing_time'])
    return res.reset_index()[['machine_id','processing_time']].groupby('machine_id',as_index = False).mean().round(3) 