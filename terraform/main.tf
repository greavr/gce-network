# ----------------------------------------------------------------------------------------------------------------------
# Enable APIs
# ----------------------------------------------------------------------------------------------------------------------
resource "google_project_service" "enable-services" {
  for_each = toset(var.services_to_enable)

  project = var.project_id
  service = each.value
  disable_on_destroy = false
}

# ----------------------------------------------------------------------------------------------------------------------
# Configure VPC
# ----------------------------------------------------------------------------------------------------------------------
module "vpc" {
  source  = "./modules/vpc"
  project_id = var.project_id
  vpc-name = var.vpc-name
  app-port = var.app-port

  depends_on = [
    google_project_service.enable-services,
  ]
}

# ----------------------------------------------------------------------------------------------------------------------
# Configure GCE SA
# ----------------------------------------------------------------------------------------------------------------------
module "gce-sa" {
  source  = "./modules/gce-sa"
  project_id = var.project_id
  gce-roles = var.gce_service_account_roles

  depends_on = [
    google_project_service.enable-services,
  ]
}

# ----------------------------------------------------------------------------------------------------------------------
# Upload Instance Code
# ----------------------------------------------------------------------------------------------------------------------
module "gcs" {
  source  = "./modules/gcs"
  project_id = var.project_id

  depends_on = [
    google_project_service.enable-services,
  ]
}

# ----------------------------------------------------------------------------------------------------------------------
# Enable Firestore
# ----------------------------------------------------------------------------------------------------------------------
module "firestore" {
  source  = "./modules/firestore"
  project_id = var.project_id
  primary-region = var.primary-region

  depends_on = [
    google_project_service.enable-services,
  ]
}