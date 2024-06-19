import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = triangle.apply(lambda row : 'Yes' if (row.x + row.y > row.z) & (row.x + row.z > row.y) & (row.y + row.z > row.x) else 'No', axis = 1)
    return triangle