import pandas as pd

def load_data(mode, last_run_time=None):
    data = {
        "id": [1, 2, 3],
        "value": [10, None, 30],
        "updated_at": ["2024-12-01", "2024-12-02", "2024-12-03"]
    }
    return pd.DataFrame(data)
