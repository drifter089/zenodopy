import os
import time
import json
from pathlib import Path
import argparse
import zenodopy

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Update Zenodo deposition with new version and files.')
    parser.add_argument('--version_tag', required=True, help='The version tag for the new release.')
    parser.add_argument('--zenodo_token', required=True, help='The Zenodo API token.')
    parser.add_argument('--dep_id', required=True, type=int, help='The Zenodo deposition ID.')
    parser.add_argument('--base_dir', required=True, help='The base directory path.')
    parser.add_argument('--metadata_file', required=True, help='The metadata JSON file path.')
    parser.add_argument('--upload_dir', required=True, help='The directory containing files to upload.')

    args = parser.parse_args()

    version_tag = args.version_tag
    zenodo_token = args.zenodo_token
    dep_id = args.dep_id
    base_dir = Path(args.base_dir)
    zenodo_metadata_file = Path(args.metadata_file)
    upload_dir = Path(args.upload_dir)

    print("Version Tag:", version_tag)

    def prepare_metadata(file_path, new_version):
        with open(file_path, "r") as file:
            zenodo_data = json.load(file)

        zenodo_data["metadata"]["version"] = new_version

        with open(file_path, "w") as file:
            json.dump(zenodo_data, file, indent=2)

    # Prepare the metadata file with the new version tag
    prepare_metadata(zenodo_metadata_file, version_tag)

    max_retries = 5

    for attempt in range(1, max_retries + 1):
        try:
            zeno = zenodopy.Client(
                sandbox=True,
                token=zenodo_token,
            )

            zeno.set_project(dep_id=dep_id)

            zeno.update(
                source=str(upload_dir),
                publish=True,
                metadata_json=str(zenodo_metadata_file),
            )
            print("Update succeeded.")
            break

        except Exception as e:
            print(f"Attempt {attempt} failed with error: {e}")

            time.sleep(2)  # Optional: Wait before retrying

            zeno._delete_project(dep_id=dep_id)

            if attempt == max_retries:
                print("Max retries reached. Exiting.")
                raise
            else:
                time.sleep(2)

if __name__ == "__main__":
    main()