# ----------------------------------------------------------------------------------------------------------------------
# Firewall Rules
# ----------------------------------------------------------------------------------------------------------------------
resource "google_compute_firewall" "fileshare-rules" {

    name = "allow-fileshare-talk"
    network = var.vpc-name

    allow {
        protocol = "tcp"
        ports = [var.app-port]
    }

    source_tags = ["gce-network"]
    target_tags = ["gce-network"]

    depends_on = [
        google_compute_network.demo-vpc
    ]
}

# ----------------------------------------------------------------------------------------------------------------------
# IAP Firewall Rule
# ----------------------------------------------------------------------------------------------------------------------
resource "google_compute_firewall" "iap" {
  name    = "allow-iap-ssh"
  network = var.vpc-name


  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["35.235.240.0/20"]

  depends_on = [
        google_compute_network.demo-vpc
    ]
}