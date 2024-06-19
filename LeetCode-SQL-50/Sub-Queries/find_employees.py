import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[~((employees.manager_id.isin(employees.employee_id)) | (employees.manager_id.isna())) & (employees.salary < 30000)][['employee_id']].sort_values(by = 'employee_id')