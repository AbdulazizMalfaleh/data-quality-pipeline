import psycopg2
import yaml

def get_connection():
    with open("config/settings.yaml") as f:
        config = yaml.safe_load(f)

    db = config["database"]

    conn = psycopg2.connect(
        host=db["host"],
        port=db["port"],
        dbname=db["dbname"],
        user=db["user"],
        password=db["password"]
    )
    return conn
