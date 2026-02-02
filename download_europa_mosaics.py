# Download Europa Galileo SSI mosaics from AWS Open Data
# Requires: boto3 (install with `pip install boto3`)
import os
import boto3
from botocore import UNSIGNED
from botocore.client import Config

# Set up S3 client for anonymous access
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

BUCKET = 'astrogeo-ard'
PREFIX = 'jupiter/europa/galileo_voyager/usgs_controlled_mosaics/'
LOCAL_DIR = './data/'

os.makedirs(LOCAL_DIR, exist_ok=True)

# List all files in the S3 bucket under the prefix
def list_files():
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=BUCKET, Prefix=PREFIX):
        for obj in page.get('Contents', []):
            key = obj['Key']
            if key.endswith('.tif'):
                yield key

def download_file(key):
    filename = os.path.basename(key)
    local_path = os.path.join(LOCAL_DIR, filename)
    if os.path.exists(local_path):
        print(f"Already downloaded: {filename}")
        return
    print(f"Downloading: {filename}")
    s3.download_file(BUCKET, key, local_path)
    print(f"Saved to: {local_path}")

if __name__ == "__main__":
    # Download the first 10 mosaics (edit as needed)
    for i, key in enumerate(list_files()):
        if i >= 10:
            break
        download_file(key)
    print("Download complete. Files saved in ./data/")
