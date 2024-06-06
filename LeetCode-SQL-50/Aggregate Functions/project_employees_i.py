import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(project,employee, on = 'employee_id').groupby('project_id', as_index = False)['experience_years'].mean().round(2).rename(columns ={'experience_years':'average_years'})