# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import json


# -----------------------------------------------------------------------------
# variables
# -----------------------------------------------------------------------------






# -----------------------------------------------------------------------------
# functions
# -----------------------------------------------------------------------------
def jprint(list_or_dict):
    print(json.dumps(list_or_dict, indent=2))


def read_json_file(json_file):
    with open(json_file, 'r') as f:
        contents = f.read()
    return json.loads(contents)