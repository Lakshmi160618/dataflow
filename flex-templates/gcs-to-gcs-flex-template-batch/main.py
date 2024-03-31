import apache_beam as beam
from apache_beam.io.textio import ReadFromText, WriteToText
from apache_beam.options.pipeline_options import PipelineOptions


def read_from_cloud_storage(argv=None):
    # Parse the pipeline options passed into the application.
    class MyOptions(PipelineOptions):
        @classmethod
        # Define custom pipeline options for input and output buckets.
        def _add_argparse_args(cls, parser):
            parser.add_argument("--input", required=True)
            parser.add_argument("--output", required=True)

    options = MyOptions()

    with beam.Pipeline(options=options) as pipeline:
        # Read content from files in Cloud Storage
        content = (
            pipeline
            | "Read Files" >> ReadFromText(options.input)
        )

        # Write content to files in Cloud Storage
        content | "Write to Output" >> WriteToText(options.output)


if __name__ == "__main__":
    read_from_cloud_storage()
