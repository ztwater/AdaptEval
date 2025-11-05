import yaml

def str_presenter(var_0, var_1):
  if len(var_1.splitlines()) > 1:  # check for multiline string
    return var_0.represent_scalar('tag:yaml.org,2002:str', var_1, style='|')
  return var_0.represent_scalar('tag:yaml.org,2002:str', var_1)

# to use with safe_dump:
yaml.representer.SafeRepresenter.add_representer(str, str_presenter)
