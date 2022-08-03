from handlers.firestore import firestore
import config as config
import os
import random
import requests
import logging
import random
import socket

## Helper functions
def GetConfig():
    """ Function to populate values from environment"""
    try:
        config.first_node = os.environ.get('first_node', True)
        config.gcp_project = os.environ.get('GCP_PROJECT', "")
        config.filename = os.environ.get('filename', "sample-file")
        config.file_chain_id = "9224"
        #config.file_chain_id = str(os.environ.get('file_chain_id', random.randint(1111,9999)))
        config.file_size = os.environ.get('file_size', 1073741824) # BYTES
        config.server_port = os.environ.get('server_port',5001)
        config.buffer_size = os.environ.get('buffer_size',1024) * 4
        config.current_instance_size = get_machine_type()
        config.current_instance_zone = get_zone()
        config.shutdown_after_transfer = os.environ.get('shutdown_after_transfer', True)
        config.server_name = socket.gethostname()

        # Build Firebase Collection
        config.firestore_collection = "gce-network"

    except Exception as e:
       # Unable to load file, quit
       logging.error(f"GetConfig error: {e}")
       quit()

def generate_big_random_bin_file(filename: str ,size: int):
    """ Generate a large file based on config.file_size requirement"""
    with open('%s'%filename, 'wb') as fout:
        fout.write(os.urandom(size)) #1

    logging.info(f'Big random binary file with size %f generated ok'%size)

def first_node():
    """ Function for the first node in the chain. This creates the sample file, calls firestore entry"""
    ## Create Sample file
    logging.info(f"First node in the chain: {config.file_chain_id}")
    send_file=str(config.file_chain_id) + "-" + config.filename
    print(f"Creating new file: {send_file}")
    generate_big_random_bin_file(filename=send_file, size=config.file_size)

    ## Set values
    #### Update these in future
    config.new_instance_size = config.current_instance_size
    config.next_instance_zone = "random"

    ## Create Firestore doc
    firestore.new_chain(doc_id=str(config.file_chain_id))

def get_zone() -> str:
    """ Read GCE metadata to get current zone, default value is local"""
    # Gather Zone Info
    instance_zone = "local"
    try: 
        url = "http://metadata.google.internal/computeMetadata/v1/instance/zone"
        metadata_flavor = {'Metadata-Flavor' : 'Google'}
        instance_zone = requests.get(url, headers = metadata_flavor).text
        logging.info(f"Instance found in zone: {instance_zone}")
    except Exception as e:
        logging.error(f"get_zone error: {e}")

    return instance_zone

def get_machine_type() -> str:
    """ Read GCE meta-data to get machine type, default value is test"""
    # Gather Instance type
    gce_machine_type = "test"
    try: 
        url = "http://metadata.google.internal/computeMetadata/v1/instance/machine-type"
        metadata_flavor = {'Metadata-Flavor' : 'Google'}
        gce_machine_type = requests.get(url, headers = metadata_flavor).text
        logging.info(f"Instance type found to be: {gce_machine_type}")
    except Exception as e:
        logging.error(f"get_machine_type error: {e}")

    return gce_machine_type

def pick_next_zone() -> str:
    """ This function chooses the next zone to deploy instance to. If config.next_zone is random will randomly choose"""

    choice = config.current_instance_zone
    # If random pic from list and validate its not the same as current zone
    if config.next_instance_zone == "random":
        # Attempt to make sure that random choice is not the same value as current zone
        while choice != config.current_instance_zone:
            choice = random.choice(config.region_list.keys())
    else:
        # Use flag for finding next value
        set_value = False
        # Itterate over keys
        for key in config.region_list:
            # Flag set, save choice
            if set_value:
                choice = key
            # Found current zone, set the flag for next itteration in dictonary
            if key == choice:
                set_value = True

    # Return value
    return choice