import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

# Define your GCP project ID and Pub/Sub topic
project_id = 'lct-dev-416808'
topic = 'projects/{}/topics/{}'.format(project_id, 'lct-demo-topic')

# Define your pipeline options
options = PipelineOptions()

# Update pipeline options for Dataflow runner
options.view_as(beam.options.pipeline_options.GoogleCloudOptions).project = project_id
options.view_as(beam.options.pipeline_options.GoogleCloudOptions).temp_location = 'gs://lct-dev-project-dataflow-temp/'
options.view_as(beam.options.pipeline_options.GoogleCloudOptions).staging_location = 'gs://lct-dev-project-dataflow-staging/staging/'
options.view_as(beam.options.pipeline_options.StandardOptions).runner = 'Dataflow'
options.view_as(beam.options.pipeline_options.GoogleCloudOptions).region = 'us-central1'  # Specify the appropriate region

# Define your pipeline
pipeline = beam.Pipeline(options=options)

# Function to extract file info from JSON payload
def extract_file_info(message):
    message_dict = json.loads(message)
    bucket = message_dict['bucket']
    file_name = message_dict['name']
    print(bucket, file_name)
    return bucket, file_name

# Function to move file to another bucket
def move_file(element):
    import apache_beam as beam  # Import beam module within the function
    bucket, file_name = element
    source_blob_uri = f"gs://{bucket}/{file_name}"
    destination_blob_uri = f"gs://target_bucket_lct_projct/{file_name}"
    
    # Copy the file
    source_blob = beam.io.gcp.gcsio.GcsIO().open(source_blob_uri)
    with beam.io.gcp.gcsio.GcsIO().open(destination_blob_uri, 'w') as dest_blob:
        dest_blob.write(source_blob.read())

    # Delete the file from the source bucket (optional)
    # beam.io.gcp.gcsio.GcsIO().delete(source_blob_uri)

    return f"File moved from {source_blob_uri} to {destination_blob_uri}"

# Read messages from the Pub/Sub topic
messages = (
    pipeline
    | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic=topic)
    | 'Extract file info' >> beam.Map(extract_file_info)
    | 'Move file to another bucket' >> beam.Map(move_file)
)

# Print the result of moving the file (for demonstration)
_ = messages | beam.Map(print)

# Run the pipeline
result = pipeline.run()
result.wait_until_finish()
