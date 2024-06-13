import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    gp = courses.groupby('class', as_index = False).count()
    return gp[gp.student >= 5][['class']]