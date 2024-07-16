import json
import os

# Function to split the JSON data into multiple files
def split_json(input_file):
    # Read the JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Loop through each entry and save it as a separate JSON file
    for entry in data:
        file_name = f"{entry['id'].strip('.')}.json"
        with open(file_name, 'w') as json_file:
            json.dump(entry, json_file, indent=4)

if __name__ == "__main__":
    # Name of the input file
    input_file = 'all.json'
    
    # Check if the file exists
    if os.path.exists(input_file):
        split_json(input_file)
        print("Files have been split successfully.")
    else:
        print(f"The file {input_file} does not exist.")
