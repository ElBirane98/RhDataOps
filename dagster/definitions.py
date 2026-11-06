# dagster/definitions.py
from pathlib import Path
from dagster_dbt import DbtCliResource, DbtProject, dbt_assets
import dagster as dg

# 1. Localiser le projet dbt (qui est à la racine du dossier rhops)
dbt_project_dir = Path(__file__).parent.parent
dbt_profiles_dir = Path.home() / ".dbt"
dbt_project = DbtProject(project_dir=dbt_project_dir, profiles_dir=dbt_profiles_dir)
dbt_project.prepare_if_dev() # Prépare le manifeste pour le développement

# 2. Créer la ressource dbt qui sera utilisée par les assets
dbt_resource = DbtCliResource(project_dir=dbt_project, profiles_dir=dbt_profiles_dir)

# 3. Transformer les modèles dbt en assets Dagster
@dbt_assets(manifest=dbt_project.manifest_path)
def rhops_dbt_assets(context: dg.AssetExecutionContext, dbt: DbtCliResource):
    # La commande "build" de dbt exécute les modèles ET les tests
    yield from dbt.cli(["build"], context=context).stream()

# 4. Enregistrer les définitions pour que Dagster les voie
defs = dg.Definitions(
    assets=[rhops_dbt_assets],
    resources={"dbt": dbt_resource},
)