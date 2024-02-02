# python-cf-gen-tf
Simple python script to generate TF code for all domains and their dns records via user API requests to NS1 ( https://my.nsone.net/ )

## Requirements 
 - Python3
 - the pip packages in requirements.txt
 - internet connection

## Setup and usage
 ```bash
 git clone https://github.com/boznius/python-ns1-gen-tf.git
 cd python-cf-gen-tf
 python3 -m venv .venv
 source .venv/bin/activate
 pip install -r requirements.txt
 # Generate a user api code and add it to api_token = '' inside of the script.
 vim/nano export_api_key.sh # fill in the api key and export it or run the bas script
 vim/nano ns1-generate-tf.py 
 # Then run the script:
 python ns1-generate-tf.py
 # This is expected to generate domain files with all the records you have inside of the terraform_files/ folder under the repository or create it if it does not exist.
 
```
