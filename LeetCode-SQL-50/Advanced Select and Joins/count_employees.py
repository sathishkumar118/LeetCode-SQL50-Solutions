import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[['employee_id','name']].merge(
        employees.groupby('reports_to').agg(
            reports_count = ('employee_id', 'count'),
            average_age = ('age',lambda x: (x + 1e-12).mean().round(0))
        ),
        left_on = 'employee_id',
        right_index = True).sort_values(by = 'employee_id')