def str_presenter(dumper, data):
    if len(data.splitlines()) > 1 or '\n' in data:  
        text_list = [line.rstrip() for line in data.splitlines()]
        fixed_data = "\n".join(text_list)
        return dumper.represent_scalar('tag:yaml.org,2002:str', fixed_data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)
