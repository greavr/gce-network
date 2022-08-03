import datetime
from google.cloud import compute_v1

from handlers.firestore import firestore
import config

def create_instance() -> str:
    """ Function creates next instance in chain """
    new_server_name = ""
    firestore.add_data(collection=config.file_chain_id,doc_id=new_server_name,data_to_add={"creating-server":datetime.datetime.now(tz=datetime.timezone.utc)})

def delete_instance() -> bool:
    """ Function to self delete instance"""
    firestore.add_data(collection=config.file_chain_id,doc_id=config.server_name,data_to_add={"shuttdown-instance":datetime.datetime.now(tz=datetime.timezone.utc)})
