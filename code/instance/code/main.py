from handlers.helpers import helpers
from handlers.recievefile import recieve_file
from handlers.gcp import gce    
from handlers.firestore import firestore
import config
import logging


if __name__ == "__main__":
    ## Setup App
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.INFO)

    helpers.GetConfig()

    # Is this the first node
    if config.first_node:
        # This is the first server in the chain, no need to setup recieving server, just create next node and send file
        # Setup values for new chain
        helpers.first_node()

    else:
        # This is a server in the chain, setup the server and await incoming file
        # Lookup next values
        firestore.lookup_next_values()
        # Start new thread for the recieving server
        recieve_file.start_server()

    