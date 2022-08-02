# ----------------------------------------------------------------------------------------------------------------------
# GCE Service Account
# ----------------------------------------------------------------------------------------------------------------------
resource "google_service_account" "gce-network-sa" {
    account_id   = "gce-network-sa"
    display_name = "gce-network-sa"
}

resource "google_project_iam_member" "service_account-roles" {
    for_each = toset(var.gce-roles)
    role    = "roles/${each.value}"
    member  = "serviceAccount:${google_service_account.gce-network-sa.email}"
    depends_on = [
        google_service_account.gce-network-sa
    ]
}
