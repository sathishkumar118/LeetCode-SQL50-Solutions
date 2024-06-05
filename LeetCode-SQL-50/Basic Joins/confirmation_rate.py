import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    return signups.set_index('user_id').join(
        (confirmations[confirmations.action == 'confirmed'].groupby('user_id').count()/confirmations.groupby('user_id').count()
        ).action).action.reset_index().fillna(0).round(2).rename(columns = {'action':'confirmation_rate'})