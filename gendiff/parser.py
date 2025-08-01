import json

import yaml


def parse_file(path):
    _, format_ = path.split('.')
    
    if format_ in ["yml", "yaml"]:
        with open(path, "r") as yaml_file:
            yaml_object = yaml.safe_load(yaml_file)
            return yaml_object

    with open(path, "r") as file:
        return json.load(file)
