from ast import Pass
import socket
import tqdm
import os
import logging

import config


def send_file(filename: str, tartget_server: str):
    """ Function to send file to target server. This then calls server shutdown"""
    try:
        # get port
        host = tartget_server
        port = config.server_port
        seperator = config.seperator
        buffer_size = config.buffer_size
        # get the file size
        filesize = os.path.getsize(filename)
        # create the client socket
        s = socket.socket()
        logging.info(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        logging.info("[+] Connected.")

        # send the filename and filesize
        s.send(f"{filename}{seperator}{filesize}".encode())

        # start sending the file
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                # read the bytes from the file
                bytes_read = f.read(buffer_size)
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure transimission in 
                # busy networks
                s.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))

        # close the socket
        s.close()
    except Exception as e:
        logging.ERROR(f"send_file error: {e}")

    # TODO ADD SERVER SHUTDOWN CODE
    if config.shutdown_after_transfer:
        # Should kill server
        Pass