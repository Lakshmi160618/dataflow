
Project Requirement:
----------------------
Once the file/object finalised/created/changed in a source bucket that should be copied/moved to the target bucket when and then it is placed in the source bucket.

The options we have:
---------------------
	1. Cloud Functions - Event based Trigger - once the object placed in the bucket - then it    will be moved to the target bucket (* Limitations are there)
	2. Using Composer/Airflow - 
	   Once the airlfow/composer evnvironment is created, usually it is not going deleted/stopped
	3. Dataflow -
	4. Dataproc
	5. Shell Script
	6. Python script on vm instance


Services Involved in this Project:
------------------------------------

1. Google Cloud Storage[Source_Bucket, Target_Bucket]
2. PubSub(Topic and Subscriber)
3. Dataflow


IAM Roles and Polocies:
------------------------
For GCS Buckets:
==============
@ Requirement Service Account(we created it)
@ 

To accomplish the task of moving objects from a source bucket to a target bucket in Google Cloud Storage (GCS) using a service account, you'll need to assign appropriate roles and policies to the service account. Here are the roles and permissions required:

@ Role - The roles/storage.objectAdmin role provides permissions to create, delete, and overwrite objects in a bucket.


Here's how you can assign roles to a service account:

Go to the Google Cloud Console: https://console.cloud.google.com/
Navigate to the "IAM & Admin" > "IAM" section.
Find the service account you want to modify and click on the pencil icon to edit its permissions.
Click "Add Member" and enter the email address of the service account.
Select the appropriate role(s) from the dropdown menu, such as roles/storage.admin or roles/storage.objectAdmin.
Click "Save" to apply the changes.

2. PubSub(Topic and Subscriber):
===================================


To accomplish the task of reading messages from a Pub/Sub topic, performing transformations, and then loading the transformed data into a Google Cloud Storage (GCS) bucket, you'll need to assign appropriate roles and permissions to the service account that your application will be using. Here are the roles and permissions required:

Pub/Sub Subscriber Role:

Assign the roles/pubsub.subscriber role to the service account for the Pub/Sub topic from which you'll be reading messages.
This role allows the service account to receive messages from the Pub/Sub topic.
Pub/Sub Publisher Role (Optional):

If your application needs to publish messages to a Pub/Sub topic, you'll need to assign the roles/pubsub.publisher role to the service account for the Pub/Sub topic.
This role allows the service account to publish messages to the Pub/Sub topic.
Storage Object Creator Role:

Assign the roles/storage.objectCreator role to the service account for the GCS bucket into which you'll be loading the transformed data.
This role grants permissions to create objects (files) in the GCS bucket.
Storage Object Viewer Role (Optional):

If you need to read objects from the GCS bucket, assign the roles/storage.objectViewer role to the service account for the GCS bucket.
This role allows the service account to list and view objects in the GCS bucket.



gsutil notification list -b gs://source_bucket_lct_projct


gsutil notification create -f json -t lct-demo-topic -e OBJECT_FINALIZE gs://source_bucket_lct_projct


bucketIdeventTimeeventTypenotificationConfigobjectGenerationobjectIdpayloadFormat
{
  "kind": "storage#object",
  "id": "source_bucket_lct_projct/190324sql.txt/1711444321119606",
  "selfLink": "https://www.googleapis.com/storage/v1/b/source_bucket_lct_projct/o/190324sql.txt",
  "name": "190324sql.txt",
  "bucket": "source_bucket_lct_projct",
  "generation": "1711444321119606",
  "metageneration": "1",
  "contentType": "text/plain",
  "timeCreated": "2024-03-26T09:12:01.135Z",
  "updated": "2024-03-26T09:12:01.135Z",
  "storageClass": "STANDARD",
  "timeStorageClassUpdated": "2024-03-26T09:12:01.135Z",
  "size": "4967",
  "md5Hash": "7sLHnwMPPxdFNOf9+l2Xqg==",
  "mediaLink": "https://storage.googleapis.com/download/storage/v1/b/source_bucket_lct_projct/o/190324sql.txt?generation=1711444321119606&alt=media",
  "crc32c": "mwZBUA==",
  "etag": "CPbawPbKkYUDEAE="
}

 

gs://source_bucket_lct_projct/260324-SessionOne.txt

pubsub - msg - payload - python read - print - json extraction - gcs uri --



The run command for this job from cloud shell:
-----------------------------------------------
python /home/gcpcloud305/dev_folder/dataflow-final.py --streaming

