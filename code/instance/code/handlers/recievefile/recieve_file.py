import socket
import tqdm
import threading
import os
import logging
import datetime

import config
from handlers.firestore import firestore

def start_server():
    """ Function to start recieving server in background thread"""
    firestore.add_data(collection=config.file_chain_id,doc_id=config.server_name,data_to_add={"starting-server":datetime.datetime.now(tz=datetime.timezone.utc)})
    x = threading.Thread( target=recieve_file, args=(0,))
    x.start()

def recieve_file(name):
    SERVER_HOST = "0.0.0.0"
    port = config.server_port
    # receive 4096 bytes each time
    BUFFER_SIZE = 4096
    SEPARATOR = config.seperator
    # TCP socket
    s = socket.socket()
    # bind the socket to our local address
    s.bind((SERVER_HOST, port))
    # enabling our server to accept connections
    # 5 here is the number of unaccepted connections that
    # the system will allow before refusing new connections
    s.listen(5)
    logging.info(f"[*] Listening as {SERVER_HOST}:{port}")
    # accept connection if there is any
    client_socket, address = s.accept() 
    # if below code is executed, that means the sender is connected
    logging.info(f"[+] {address} is connected.")
    firestore.add_data(collection=config.file_chain_id,doc_id=config.server_name,data_to_add={"client-connected":datetime.datetime.now(tz=datetime.timezone.utc)})

    # receive the file infos
    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)
    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open("file/" + filename, "wb") as f:
        while True:
            # Log data transfer started
            firestore.add_data(collection=config.file_chain_id,doc_id=config.server_name,data_to_add={"transfer-started":datetime.datetime.now(tz=datetime.timezone.utc)})
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the client socket
    client_socket.close()
    firestore.add_data(collection=config.file_chain_id,doc_id=config.server_name,data_to_add={"transfer-complete":datetime.datetime.now(tz=datetime.timezone.utc)})
    # close the server socket
    s.close()
    logging.info(f"File transfer complete: 'file/{filename}'")