from google.cloud import pubsub_v1
import os

def create_topic(project_id, topic_name, credentials_path):
    """
    Creates a new Pub/Sub topic.

    Args:
        project_id (str): The Google Cloud project ID.
        topic_name (str): The name of the new topic to create.
        credentials_path (str): The path to the service account key file.

    Returns:
        None
    """
    # Set the environment variable for authentication
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

    # Initialize a Pub/Sub client
    publisher_client = pubsub_v1.PublisherClient()

    # Create the fully qualified topic name
    topic_path = publisher_client.topic_path(project_id, topic_name)

    # Create the topic
    topic = publisher_client.create_topic(request={"name": topic_path})

    print(f"Topic '{topic.name}' created")

# Replace 'your-project-id' with your Google Cloud project ID
project_id = "lct-dev-416808"

# Replace 'your-topic-name' with the desired name for your topic
topic_name = "lct-demo-topic"

# Replace 'path/to/service_account_key.json' with the path to your service account key file
credentials_path = r"D:\dataflow\dataflow\project_two\secrets\lct-dev-project-bucket-creator-sa.json"

# Call the function to create the topic
create_topic(project_id, topic_name, credentials_path)
