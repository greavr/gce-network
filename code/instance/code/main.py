from socket import send_fds
import time
import os

from handlers.helpers import helpers
from handlers.sendfile import sendfile
from handlers.recievefile import recieve_file
import config


if __name__ == "__main__":
    ## Setup App
    helpers.GetConfig()

    # Start new thread for the recieving server
    recieve_file.start_server()
    
    time.sleep(5)

    # Is this the first node
    if config.first_node:
        helpers.first_node()