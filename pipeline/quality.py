def run_quality_checks(df):
    return {
        "row_count": int(len(df)),
        "nulls": {
            col: int(count)
            for col, count in df.isnull().sum().to_dict().items()
        },
        "duplicates": int(df.duplicated().sum())
    }
