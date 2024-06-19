import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    emp_with_primary_flag = employee[employee.primary_flag == 'Y']
    return pd.concat(
        [
            emp_with_primary_flag,
            employee[~employee.employee_id.isin(
                emp_with_primary_flag.employee_id
                )].groupby(
                    'employee_id',
                    as_index = False).filter(
                        lambda x: len(x) == 1
                        )]).drop(
                            columns = ['primary_flag']
                            )