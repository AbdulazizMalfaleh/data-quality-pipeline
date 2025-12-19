import time
from typing import Dict, Any
import pandas as pd


def calculate_metrics(
    df: pd.DataFrame,
    start_time: float,
    cost_per_second: float,
    cost_per_mb: float
) -> Dict[str, Any]:
    """
    Calculate performance and cost metrics for a data pipeline run.

    Metrics:
    - Execution time (seconds)
    - Data size (MB)
    - Estimated cost (time-based + data-based)
    """

    execution_time = time.time() - start_time
    data_size_mb = df.memory_usage(deep=True).sum() / (1024 ** 2)

    time_cost = execution_time * cost_per_second
    data_cost = data_size_mb * cost_per_mb
    estimated_cost = time_cost + data_cost

    return {
        "execution_time_sec": round(float(execution_time), 4),
        "data_size_mb": round(float(data_size_mb), 6),
        "cost_breakdown": {
            "time_cost": round(float(time_cost), 8),
            "data_cost": round(float(data_cost), 8)
        },
        "estimated_cost": round(float(estimated_cost), 8)
    }
