from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(retries=3)
def extract_from_gcs(dataset_file: str) -> Path:
    """Download trip data from GCS"""
    gcs_path = f"data/{dataset_file}.parquet"
    gcs_block = GcsBucket.load("mental-health-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"./data/from_gcs/")
    return Path(f"./data/from_gcs/{gcs_path}")
    


@task()
def transform(path: Path) -> pd.DataFrame:
    """Data cleaning"""
    df = pd.read_parquet(path)
    return df


@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""
    gcp_credentials_block = GcpCredentials.load("gcp-creds")

    df.to_gbq(
        destination_table="mental-health-analysis-395019.mentalhealth_staging.mental_health_table_1",
        project_id="mental-health-analysis-395019",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        if_exists="append",
    )


@flow()
def etl_gcs_to_bq():
    """Main ETL flow to load data into Big Query"""
    filename = 'mental-health-data'
    version = 1
    dataset_file = f"{filename}_version_{version}"

    path = extract_from_gcs(dataset_file)
    df = transform(path)
    write_bq(df)


if __name__ == "__main__":
    etl_gcs_to_bq()