import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby('departmentId').salary.rank(method = 'dense', ascending = False)
    employee = employee.loc[employee['rank'] <= 3].merge(
        department,
        left_on = 'departmentId',
        right_on = 'id')[['name_y','name_x','salary']]
    employee.columns = ['Department','Employee','Salary']
    return employee