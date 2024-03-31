Dataflow flex template: Getting started sample
Before you begin
Make sure you have followed the Dataflow setup instructions.

Create a Cloud Storage bucket
export BUCKET="your--bucket"
gsutil mb gs://$BUCKET
create an Artifact Registry repository
export REGION="us-central1"
export REPOSITORY="your-repository"

gcloud artifacts repositories create $REPOSITORY \
    --repository-format=docker \
    --location=$REGION
Build the template
export PROJECT="project-id"

gcloud dataflow flex-template build gs://$BUCKET/getting_started_py.json \
    --image-gcr-path "$REGION-docker.pkg.dev/$PROJECT/$REPOSITORY/getting-started-py:latest" \
    --sdk-language "PYTHON" \
    --flex-template-base-image "PYTHON3" \
    --py-path "." \
    --metadata-file "metadata.json" \
    --env "FLEX_TEMPLATE_PYTHON_PY_FILE=getting_started.py" \
    --env "FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE=requirements.txt"
Run the template
gcloud dataflow flex-template run "flex-`date +%Y%m%d-%H%M%S`" \
    --template-file-gcs-location "gs://$BUCKET/getting_started_py.json" \
    --region $REGION \
    --parameters output="gs://$BUCKET/output-"
What's next?
For more information about building and running flex templates, see 📝 Use Flex Templates.


Extra-info:
gcloud dataflow flex-template build gs://flex-template-bucket-demo2/second-pipeline-py.json \
 --image-gcr-path "us-central1-docker.pkg.dev/lct-dev-416808/flex-repo-to-mv-gcs-gcs/second-pipeline-python:latest" \
 --sdk-language "PYTHON" \
 --flex-template-base-image "PYTHON3" \
 --metadata-file "metadata.json" \
 --py-path "." \
 --env "FLEX_TEMPLATE_PYTHON_PY_FILE=second-pipeline.py" \
 --env "FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE=requirements.txt"
 
gcloud dataflow flex-template run "second-pipeline-$(date +%Y%m%d-%H%M%S)" \
 --template-file-gcs-location "gs://flex-template-bucket-demo2/second-pipeline-py.json" \
 --parameters input="gs://source_bucket_lct_projct/temparature.csv",output="gs://target_bucket_lct_projct/outputhere-" \
 --region "us-central1"