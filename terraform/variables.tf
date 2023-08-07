locals {
  data_lake_bucket = "mentalhealth_data"
}

variable "project" {
  description = "Your GCP Project ID"
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default = "europe-west1"
  type = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET_1" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
  default = "mentalhealth_staging"
}

variable "BQ_DATASET_2" {
  description = "BigQuery Dataset that transformed data (from GCS) will be written to"
  type = string
  default = "mentalhealth_prod"
}


