import os
import subprocess
import pandas as pd
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path



@task(retries=3)
def fetch(dataset_name: str) -> pd.DataFrame:
    """Read data from kaggle into pandas DataFrame"""
    filename = 'mental-health-data'
    # Authenticate with the Kaggle API
    api = KaggleApi()
    api.authenticate()
    # Download the dataset
    subprocess.run(["kaggle", "datasets", "download", "-d", dataset_name])
    # Unzip the file if necessary
    if not os.path.exists(filename):
        os.system(f'unzip {filename}.zip')
    df = pd.read_csv('mental_heath_data.csv')
    return df

@task(log_prints=True)
def clean(df: pd.DataFrame) -> pd.DataFrame:
    """ fix some issues in the dataframe"""
    # select only the non-numeric columns using the select_dtypes() method
    non_numeric_columns = df.select_dtypes(exclude='int').columns
    # Apply str.lower() function to all non-numeric columns except 'age'
    df[non_numeric_columns] = df[non_numeric_columns].applymap(lambda x: x.lower() if isinstance(x, str) else x)
    # Use the replace() method to change some gender values
    df['Gender'] = df['Gender'].replace({'m': 'male', 'f': 'female'})
    #change timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    #print(df.head(5))
    return df


@task()
def write_local(df: pd.DataFrame, dataset_file: str) -> Path:
    """Write DataFrame out locally as parquet file"""
    path = Path(f"data/{dataset_file}.parquet")
    df.to_parquet(path, compression="gzip")
    return path


@task()
def write_gcs(path: Path) -> None:
    """Upload local parquet file to GCS"""
    gcs_block = GcsBucket.load("mental-health-gcs")
    gcs_block.upload_from_path(from_path=path, to_path=path)
    return


@flow()
def etl_web_to_gcs() -> None:
    """The main ETL function"""
    dataset_name = "jameswachuka/mental-health-data"
    filename = 'mental-health-data'
    version = 1
    dataset_file = f"{filename}_version_{version}"

    df = fetch(dataset_name)
    df_clean = clean(df)
    path = write_local(df_clean, dataset_file)
    write_gcs(path)
    

if __name__ == "__main__":
    etl_web_to_gcs()





