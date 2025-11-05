def yaml_multiline_string_presenter(dumper, data):
    if len(data.splitlines()) > 1:
        # Pyyaml does not allow trailing space at the end of line for block string
        data = '\n'.join([line.rstrip() for line in data.strip().splitlines()])
        # Pyyaml does not allow tab in a block string
        data = data.replace('\t', '    ')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, yaml_multiline_string_presenter)
yaml.representer.SafeRepresenter.add_representer(str, yaml_multiline_string_presenter)
