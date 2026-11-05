"""
Ingestion de la couche Bronze : charge le CSV brut dans DuckDB.
"""
import duckdb
from pathlib import Path

DB_PATH = "dev.duckdb"
CSV_PATH = "data/employees.csv"

def main():
    if not Path(CSV_PATH).exists():
        raise FileNotFoundError(f"❌ CSV introuvable : {CSV_PATH}")

    print(f"🔄 Connexion à DuckDB : {DB_PATH}")
    con = duckdb.connect(DB_PATH)
    
    con.execute("CREATE SCHEMA IF NOT EXISTS bronze")

    print(f"🔄 Ingestion de {CSV_PATH}...")
    con.execute(f"""
        CREATE OR REPLACE TABLE bronze.employees_raw AS
        SELECT * FROM read_csv_auto('{CSV_PATH}', header=true)
    """)

    count = con.execute("SELECT COUNT(*) FROM bronze.employees_raw").fetchone()[0]
    cols = con.execute("DESCRIBE bronze.employees_raw").df()

    print(f"\n✅ {count} lignes ingérées dans bronze.employees_raw")
    print(f"✅ {len(cols)} colonnes détectées\n")
    print(cols[["column_name", "column_type"]].to_string(index=False))
    print()

    con.close()

if __name__ == "__main__":
    main()