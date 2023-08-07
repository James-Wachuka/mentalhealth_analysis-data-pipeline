from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

# alternative to creating GCP blocks in the UI
# copy your own service_account_info dictionary from the json file you downloaded from google
# IMPORTANT - do not store credentials in a publicly available repository!

# enter your credentials from the json file
credentials_block = GcpCredentials(
    service_account_info={
 # enter your cgcp credentials
}

)
credentials_block.save("gcp-creds", overwrite=True)


bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load("gcp-creds"),
    bucket="mentalhealth_data_mental-health-analysis-395019",  # insert your  GCS bucket name
)

bucket_block.save("mental-health-gcs", overwrite=True)

