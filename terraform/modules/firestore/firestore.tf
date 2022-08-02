# ----------------------------------------------------------------------------------------------------------------------
# Create Firestore
# ----------------------------------------------------------------------------------------------------------------------
resource "google_app_engine_application" "gce-network" {
  project     = var.project_id
  location_id = var.primary-region
  database_type = "CLOUD_FIRESTORE"
}