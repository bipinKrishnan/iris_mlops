import yaml

def open_yaml(yaml_path: str) -> dict:
    """
    Opens the yaml file and returns the contents

    Args:
      yaml_path(str): path to the yaml file

    Returns:
      content(dict): contents of the yaml file
    """
    with open(yaml_path) as f:
        content = yaml.safe_load(f)
    return content