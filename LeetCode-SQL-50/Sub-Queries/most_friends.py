import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    res = pd.concat([request_accepted["requester_id"], request_accepted["accepter_id"]])
    r = res.value_counts().sort_values(ascending = False).head(1)
    return pd.DataFrame({"id" : r.index.to_list(), "num" : r.to_list()})