from asyncore import read
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import config
import datetime
import logging

if not firebase_admin._apps:
    """ Build credentials using application defaul credentials """
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {'projectId': config.gcp_project,})

    logging.info(f"Built credentials for project {config.gcp_project}")

    config.firestore_client = firestore.client()

def new_chain(doc_id: str) -> bool:
    """ Function to create new document with standard info """
    try:
        ref_doc = config.firestore_client.collection(config.firestore_collection).document(doc_id)
        # Add default values
        data_to_add = {}
        data_to_add['created'] = datetime.datetime.now(tz=datetime.timezone.utc)
        data_to_add['start-zone'] = config.current_instance_zone
        data_to_add['file-name'] = config.filename
        data_to_add['file-size'] = config.file_size
        data_to_add['current-instance-size'] = config.current_instance_size
        data_to_add['new_instance_size'] = config.new_instance_size
        data_to_add['next_instance_zone'] = config.next_instance_zone

        ref_doc.set(data_to_add)
        logging.info(f"Created New Record: {config.firestore_collection}, for document {doc_id}")
        return True
    except Exception as e:
       logging.error(f"new_chain error: {e}")
       return False
        

def add_data(collection: str, data_to_add: dict, doc_id: str) -> bool:
    """ Function to add dictory values to document """
    # try:
    ref_doc = config.firestore_client.collection(collection).document(doc_id)
    ref_doc.set(data_to_add)
    logging.info(f"Added values: {data_to_add} to document {doc_id} in collection: {collection}")
    return True
    # except Exception as e:
    #     logging.error(f"add_data error: {e}")
    #     return False
    
def read_data(collection: str, doc_id: str, key_value: str ) -> str:
    """Function to lookup values based on key_value in specific doc_id. Collection is set at application level"""
    result = ""
    try:
        # Gather the doc
        ref_doc = config.firestore_client.collection(collection).document(doc_id)
        doc = ref_doc.get()
        # Itterate values
        if doc.exists:
            result = doc.to_dict()[key_value]
            logging.info(f"Value found for {key_value} : {result}")
        else:
            logging.error(f"Document: {doc_id} not found in collection: {collection}")

    except Exception as e:
       logging.error(f"read_data error: {e}")
    
    return result

def lookup_next_values() -> bool:
    """Function to lookup values for new_instance_size and next_instance_zone""" 
    config.new_instance_size = read_data(collection=config.firestore_collection,doc_id=config.file_chain_id, key_value="new_instance_size")
    config.next_instance_zone = read_data(collection=config.firestore_collection,doc_id=config.file_chain_id, key_value="next_instance_zone")