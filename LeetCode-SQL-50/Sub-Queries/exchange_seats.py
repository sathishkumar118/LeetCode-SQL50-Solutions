import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    def swap_ids(id):
        if id % 2 != 0 and id == len(seat):
            return id
        elif id % 2 != 0:
            return id + 1
        return id - 1
    seat.id = seat.id.apply(swap_ids)
    return seat.sort_values(by = 'id')