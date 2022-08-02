# ----------------------------------------------------------------------------------------------------------------------
# Create GCS Bucket
# ----------------------------------------------------------------------------------------------------------------------
resource "google_storage_bucket" "instance-code" {
  name =  format("%s-%s", var.project_id, "instance-code")
  uniform_bucket_level_access = true
}

# Create Zip file
data "archive_file" "instance_code" {
  type        = "zip"
  output_path = "${path.module}/code.zip"
  source_dir = "../code/instance/code"
}

resource "google_storage_bucket_object" "code" {
  name   = "code.zip"
  bucket = google_storage_bucket.instance-code.name
  source = "${path.module}/code.zip"

  depends_on = [
    data.archive_file.instance_code,
    google_storage_bucket.instance-code
  ]
}