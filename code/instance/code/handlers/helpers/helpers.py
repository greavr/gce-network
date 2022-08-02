from handlers.sendfile import sendfile
import config as config
import os

## Helper functions
def GetConfig():
    try:
        config.first_node = os.environ.get('first_node', True)
        config.gcp_project = os.environ.get('GCP_PROJECT', "")
        config.filename = os.environ.get('filename', "sample-file")
        config.file_chain_id = os.environ.get('file_chain_id', "01")
        config.file_size = os.environ.get('file_size', 1073741824) # BYTES
        config.instance_size = os.environ.get('instance_size',"e2-small")
        config.server_port = os.environ.get('server_port',5001)
        config.buffer_size = os.environ.get('buffer_size',1024) * 4
    except Exception as e:
       # Unable to load file, quit
       print(e)
       quit()

def generate_big_random_bin_file(filename,size):
    with open('%s'%filename, 'wb') as fout:
        fout.write(os.urandom(size)) #1
    print (f'Big random binary file with size %f generated ok'%size)
    pass

def first_node():
    ## Create Sample file
    print(f"First node in the chain: {config.file_chain_id}")
    send_file=config.file_chain_id + "-" + config.filename
    print(f"Creating new file: {send_file}")
    generate_big_random_bin_file(filename=send_file, size=config.file_size)

    ## Now send file
    sendfile.send_file(filename=send_file)
    