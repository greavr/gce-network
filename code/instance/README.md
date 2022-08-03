# Instance code

This code is designed to run on the instance. It handles the following: 

 - First in chain creates file of set size (using random garbage as content)
 - sets new instance class to be the same as current
 - Created the target instance zone to be random
 - After instance is created transfers the file to target server
 - After transfer is complete instance self terminates


## Fire store entries
- Start of the chain:
  - created date/time
  - start zone
  - file name
  - file size
  - current node-type
  - sets next instance zone to random
  - sets new instance size to same as current
- Create new instance:
  - history:
    - instance location
    - instance created
- Transfer 
## Python Transfer
 - Using Sockets and tqdm

## Data to be logged:
 - [ ] Instance created Timestamp
 - [ ] Instance name & region
 - [ ] Instance Size & Network flag
 - [ ] File transfer started
   - [ ] Optional File transfer %
 - [ ] File transfer complete
 - [ ] Stream ID

## Instance creation
 - In target VPC
 - Size and spec to be read from next region / zone location. Else default to template standard (terraform flag?)
 - Boot strap code deployment


## TODO:
 - File transfer method
 - Reporting mechanism (Firestore / Stackdriver / Other)
 - File generation (at start)
 - Instance name structure (**{region}-{class}-{streamid}** i.e. ***us-west2-n2-01***

 ## Run Code Locally
```
pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
GCP_PROJECT=$(gcloud config get project)
pip3 install -r code/requirements.txt
python3 code/main.py
```
Then you can browse the code [locally](http://localhost:8080).<br /><br />
**Deactivate the environment** 
Run the following command
```
deactivate
```