import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Compile the regex pattern for efficiency
    pattern = re.compile(r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$')
    
    # Use the compiled pattern to filter valid emails
    valid_emails_mask = users['mail'].apply(lambda x: bool(pattern.match(x)))
    
    return users.loc[valid_emails_mask]