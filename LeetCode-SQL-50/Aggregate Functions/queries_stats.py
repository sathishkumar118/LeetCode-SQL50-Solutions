import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    new_round = lambda x: round(x + 1e-9, 2)
    queries['quality'] = (queries.rating/queries.position)
    queries['poor_query_percentage'] = (queries.rating < 3)*100
    return queries[queries.query_name != ''].groupby('query_name')[['quality','poor_query_percentage']].mean().apply(new_round).reset_index()