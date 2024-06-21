import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Sort salaries in descending order and drop duplicates
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if there are at least two unique salaries
    if len(sorted_salaries) > 1:
        second_highest = sorted_salaries.iloc[1]
    else:
        second_highest = None
        
    # Return the result in the required format
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})