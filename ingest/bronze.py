import duckdb
from pathlib import Path
import os

DB_PATH = "dev.duckdb"

def main():
    con = duckdb.connect(DB_PATH)
    con.execute("CREATE SCHEMA IF NOT EXISTS bronze")

    # On vérifie si on est sur GitHub Actions ou en local
    use_minio = os.getenv("USE_MINIO", "true").lower() == "true"

    if use_minio:
        print("🔄 Ingestion depuis MinIO (S3)...")
        con.execute("INSTALL httpfs;")
        con.execute("LOAD httpfs;")
        con.execute("""
            CREATE OR REPLACE SECRET minio_secret (
                TYPE s3, KEY_ID 'minioadmin', SECRET 'minioadmin',
                ENDPOINT 'localhost:9000', URL_STYLE 'path', USE_SSL false
            );
        """)
        file_path = "s3://rhops-data/employees.csv"
    else:
        print("🔄 Ingestion depuis le fichier local (CI/CD)...")
        file_path = "data/employees.csv"

    con.execute(f"""
        CREATE OR REPLACE TABLE bronze.employees_raw AS
        SELECT * FROM read_csv_auto('{file_path}', header=true)
    """)

    count = con.execute("SELECT COUNT(*) FROM bronze.employees_raw").fetchone()[0]
    print(f"✅ {count} lignes ingérées dans bronze.employees_raw")
    con.close()

if __name__ == "__main__":
    main()