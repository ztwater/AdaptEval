import yaml

def fix_pyyaml():
    """DOCSTRING"""

    # Credits for the code in this function:
    # https://stackoverflow.com/a/33300001

    def str_presenter(dumper, data):
        """DOCSTRING"""

        if len(data.splitlines()) > 1:
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")

        return dumper.represent_scalar("tag:yaml.org,2002:str", data)
    
    yaml.representer.SafeRepresenter.add_representer(str, str_presenter)
