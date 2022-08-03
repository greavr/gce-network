# Application Variables
gcp_project = ""
first_node = ""
filename = ""
file_size = ""
file_chain_id = ""
firestore_collection = ""
firestore_client = ""
new_instance_size = ""
next_instance_zone = ""
current_instance_zone = ""
current_instance_size = ""
server_port = ""
buffer_size = ""
shutdown_after_transfer = ""
server_name = ""
seperator = "<SEPERATOR>"
region_list = {
    "asia-east1-a" : ["E2", "N2", "N2D", "T2D", "N1", "M1", "C2", "C2D"],
    "asia-east2-a" : ["E2", "N2", "N2D", "N1", "C2"],
    "asia-northeast1-a" : ["E2", "N2", "N2D", "N1", "M1", "M2", "C2", "A2"],
    "asia-northeast2-a" : ["E2", "N1", "N2", "N2D", "M1", "C2"],
    "asia-northeast3-a" : ["E2", "N2", "N1", "M1", "M2", "C2", "A2"],
    "asia-south1-a" : ["E2", "N2", "N2D", "N1", "M1", "M2", "C2"],
    "asia-south2-a" : ["E2", "N1", "N2", "M1", "M2", "C2"],
    "asia-southeast1-a" : ["E2", "N2", "N2D", "T2D", "N1", "M1", "C2", "C2D"],
    "asia-southeast2-a" : ["E2", "N2", "N1", "M1"],
    "australia-southeast1-a" : ["E2", "N2", "N2D", "T2D", "N1", "C2", "M1", "M2"],
    "australia-southeast2-b" : ["E2", "N1", "N2", "M1"],
    "europe-central2-a" : ["E2", "N2", "N1"],
    "europe-north1-a" : ["E2", "N2", "N2D", "N1", "C2"],
    "europe-southwest1-a" : ["E2", "N2", "N2D"],
    "europe-west1-d" : ["E2", "N2", "N2D", "T2D", "N1", "M1", "M2", "C2", "C2D"],
    "europe-west2-c" : ["E2", "N2", "N2D", "T2D", "N1", "M1", "C2", "C2D"],
    "europe-west3-a" : ["E2", "N2", "N2D", "T2D", "N1", "M1", "M2", "C2"],
    "europe-west4-a" : ["E2", "N2", "N2D", "T2D", "T2A", "N1", "M1", "M2", "C2", "C2D", "A2"],
    "europe-west6-c" : ["E2", "N2", "N1", "M1", "C2"],
    "europe-west8-a" : ["E2", "N2", "N2D", "M2"],
    "europe-west9-a" : ["E2", "N2", "N2D"],
    "northamerica-northeast1-b" : ["E2", "N2", "N2D", "N1", "M1", "M2", "C2"],
    "northamerica-northeast2-a" : ["E2", "N2", "N1", "M1"],
    "southamerica-east1-b" : ["E2", "N2", "N2D", "T2D", "N1", "M1", "M2", "C2"],
    "southamerica-west1-b" : ["E2", "N2", "C2", "M1"],
    "us-central1-a" : ["E2", "N2", "N2D", "T2D", "T2A", "N1", "M1", "M2", "C2", "C2D", "A2"],
    "us-east1-d" : ["E2", "N2", "N2D", "T2D", "N1", "M1", "C2", "C2D"],
    "us-east4-a" : ["E2", "N2", "N2D", "T2D", "N1", "M1", "M2", "C2", "C2D"],
    "us-east5-a" : ["E2", "N2", "N2D", "C2"],
    "us-south1-a" : ["E2", "N2"],
    "us-west1-b" : ["E2", "N2", "N2D", "T2D", "N1", "M1", "C2", "A2"],
    "us-west2-b" : ["E2", "N2", "N2D", "N1", "M1", "C2"],
    "us-west3-a" : ["E2", "N1", "N2", "C2"],
    "us-west4-b" : ["E2", "N2", "N2D", "N1", "C2", "T2D", "M1", "M2", "A2"]
}