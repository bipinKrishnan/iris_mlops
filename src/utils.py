import yaml

def open_yaml(yaml_path):
    with open(yaml_path) as f:
        content = yaml.safe_load(f)
    return content