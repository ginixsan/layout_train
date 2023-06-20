import json

def check_coco_annotations(file_path):
    # Open and load the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Define the keys that should be present in each annotation
    required_keys = ['id', 'image_id', 'category_id', 'iscrowd', 'bbox', 'area', 'segmentation']

    # Iterate over each annotation
    for i, annotation in enumerate(data['annotations'], start=1):
        # Check each key
        for key in required_keys:
            if key not in annotation:
                print(f"Annotation {i} is missing key: {key}")

    print("Annotation check complete.")

# Call the function on your file
check_coco_annotations('prodigy-coco.json')