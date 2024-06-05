import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    return employee.set_index('empId').join(bonus.set_index('empId'), how = 'left').drop(index = bonus[bonus.bonus >= 1000].empId)[['name','bonus']]