import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts = pd.concat([accounts,pd.DataFrame({'account_id' : [None, None, None], 'income' : [10000,30000,60000]})])
    def get_category(income):
        if income < 20000:
            return 'Low Salary'
        elif income <= 50000:
            return 'Average Salary'
        else:
            return 'High Salary'
    accounts['category'] = accounts.income.apply(get_category)
    return accounts.groupby('category', as_index = False).agg(accounts_count = ('account_id', 'count'))