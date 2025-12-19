import time
import yaml
from pipeline.loader import load_data
from pipeline.quality import run_quality_checks
from pipeline.metrics import calculate_metrics

def run_pipeline():
    with open("config/settings.yaml") as f:
        config = yaml.safe_load(f)

    mode = config["pipeline"]["mode"]
    last_run_time = config["pipeline"]["last_run_time"]

    start_time = time.time()

    df = load_data(mode, last_run_time)
    quality_issues = run_quality_checks(df)

    metrics = calculate_metrics(
        df,
        start_time,
        config["cost"]["cost_per_second"],
        config["cost"]["cost_per_mb"]
    )

    return {
        "mode": mode,
        "rows": len(df),
        "quality": quality_issues,
        "metrics": metrics
    }


if __name__ == "__main__":
    result = run_pipeline()
    print(result)
    input("اضغط Enter للخروج...")
