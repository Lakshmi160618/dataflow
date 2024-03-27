from google.cloud import storage

def create_bucket(bucket_name, service_account_key_file):
    """
    Creates a new Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the new bucket to create.
        service_account_key_file (str): The path to the service account key file.

    Returns:
        None
    """
    # Initialize a client with the service account key file
    storage_client = storage.Client.from_service_account_json(service_account_key_file)

    # Define the location (region) for the bucket
    location = "us-west1"

    # Create the bucket with the desired name and location
    bucket = storage_client.create_bucket(bucket_name, location=location)

    print(f"Bucket '{bucket_name}' created at location '{location}'")

# Replace 'your-bucket-name' with the desired name for your bucket
bucket_name = "target_bucket_lct_projct"

# Replace 'path/to/service_account_key.json' with the actual path to your service account key file
service_account_key_file = r"D:\dataflow\dataflow\project_two\secrets\lct-dev-project-bucket-creator-sa.json"

# Call the function to create the bucket
create_bucket(bucket_name, service_account_key_file)
