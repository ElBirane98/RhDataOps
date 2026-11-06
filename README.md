\# rhops — Pipeline DataOps pour l'Analytique RH



Pipeline de données de bout en bout (End-to-End) construit pour analyser les données RH (Turnover, Attrition, etc.) en utilisant une stack moderne et locale.



\## 🏗️ Architecture Medallion

\- \*\*Bronze\*\* : Ingestion brute du CSV via Python (`duckdb`).

\- \*\*Silver\*\* : Nettoyage et standardisation via `dbt` (vue `stg\_employees`).

\- \*\*Gold\*\* : Modélisation en étoile (table de dimension `dim\_employees` et table de faits `fct\_hr\_metrics`).

- **Stockage Objet (Data Lake)** : MinIO (compatible S3) pour stocker les fichiers bruts.
- **Ingestion** : Python (lit depuis MinIO ou localement selon l'environnement).
- **Transformation** : dbt + DuckDB (Architecture Medallion).
...



\## 🛠️ Stack Technique

\- \*\*Stockage \& Compute\*\* : DuckDB

\- \*\*Transformation\*\* : dbt Core

\- \*\*Ingestion\*\* : Python (Pandas, DuckDB)

\- \*\*Qualité\*\* : Tests dbt automatisés

\- \*\*Visualisation\*\* (à venir) : Power BI



\## 🚀 Comment lancer le projet

```bash

\# 1. Activer l'environnement

venv\\Scripts\\activate



\# 2. Lancer l'ingestion Bronze

python ingest\\bronze.py



\# 3. Construire et tester les modèles dbt

dbt build

