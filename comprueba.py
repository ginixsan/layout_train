import json

def inspect_annotations(file_path, ids):
    with open(file_path, 'r') as f:
        data = json.load(f)

    for i in ids:
        for annotation in data['annotations']:
            if annotation['id'] == i:
                print(f"Annotation {i}: {annotation}")

# Provide the IDs of the problematic annotations
ids_to_inspect = [189, 190, 341, 342, 410]

# Call the function on your file
inspect_annotations('prodigy-coco.json', ids_to_inspect)