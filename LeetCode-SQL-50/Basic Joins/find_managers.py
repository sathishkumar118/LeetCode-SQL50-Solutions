import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    return employee[employee.id.isin(employee.managerId.value_counts()[employee.managerId.value_counts() >= 5].index)][['name']]