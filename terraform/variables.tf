# ----------------------------------------------------------------------------------------------------------------------
# Variables
# ----------------------------------------------------------------------------------------------------------------------
# App Port
variable "app-port" {
  type = string
  description = "Port used to share file"
  default = "5001"
}

# Default region
variable "primary-region" {
  type = string
  description = "Default region for app engine and thread start"
  default = "us-west1"
}

# GCP Project Name
variable "project_id" {
    type = string
}

variable "vpc-name" {
    type = string
    description = "Custom VPC Name"
    default = "default"
}

# Service to enable
variable "services_to_enable" {
    description = "List of GCP Services to enable"
    type    = list(string)
    default =  [
        "compute.googleapis.com",
        "iap.googleapis.com",
        "cloudresourcemanager.googleapis.com",
        "iam.googleapis.com",
        "logging.googleapis.com",
        "monitoring.googleapis.com",
        "opsconfigmonitoring.googleapis.com",
        "serviceusage.googleapis.com",
        "stackdriver.googleapis.com",
        "servicemanagement.googleapis.com",
        "servicecontrol.googleapis.com",
        "storage.googleapis.com",
        "firestore.googleapis.com"
    ]
}

# Extra GCE SA Roles
variable "gce_service_account_roles" {
    description = "GCE Service Account Roles"
    type        = list(string)
    default     = [
        "logging.logWriter",
        "monitoring.metricWriter",
        "monitoring.dashboardEditor",
        "stackdriver.resourceMetadata.writer",
        "opsconfigmonitoring.resourceMetadata.writer",
        "compute.networkViewer",
        "datastore.user"
    ]
}