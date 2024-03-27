from google.cloud import pubsub_v1

def create_topic(service_account_key_path, project_id, topic_name):
    # Initialize the Pub/Sub publisher client with the service account key
    publisher_client = pubsub_v1.PublisherClient.from_service_account_json(service_account_key_path)

    # Create the fully qualified topic name
    topic_path = publisher_client.topic_path(project_id, topic_name)

    # Create the topic
    topic = publisher_client.create_topic(request={"name": topic_path})

    print(f"Pub/Sub topic '{topic_name}' created successfully.")

if __name__ == "__main__":
    # Replace 'path/to/service-account-key.json' with the path to your service account key file
    service_account_key_path = 'path/to/service-account-key.json'
    # Replace 'your-project-id' with your Google Cloud project ID
    project_id = 'your-project-id'
    # Replace 'your-topic-name' with the desired name for your Pub/Sub topic
    topic_name = 'your-topic-name'

    create_topic(service_account_key_path, project_id, topic_name)
