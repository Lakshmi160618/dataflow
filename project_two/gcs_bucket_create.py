from google.cloud import storage

def create_bucket(service_account_key_path, bucket_name, location="us-central1"):
    # Initialize the GCS client with the service account key
    storage_client = storage.Client.from_service_account_json(service_account_key_path)

    # Create the bucket
    bucket = storage_client.create_bucket(bucket_name, location=location)

    print(f"Bucket '{bucket_name}' created successfully.")

if __name__ == "__main__":
    # Replace 'path/to/service-account-key.json' with the path to your service account key file
    service_account_key_path = 'path/to/service-account-key.json'
    
    # Replace 'source-bucket-name' with the desired name for the source bucket
    source_bucket_name = 'source-bucket-name'
    # Replace 'target-bucket-name' with the desired name for the target bucket
    target_bucket_name = 'target-bucket-name'

    create_bucket(service_account_key_path, source_bucket_name)
    create_bucket(service_account_key_path, target_bucket_name)
