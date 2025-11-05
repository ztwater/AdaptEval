'''
json : json to extract value from if exists
path : details.detail.first_name
            empty path represents root

returns a tuple (boolean, object)
        boolean : True if path exists, otherwise False
        object : the object if path exists otherwise None

'''
def get_json_value_at_path(json, path=None, default=None):

    if not bool(path):
        return True, json
    if type(json) is not dict :
        raise ValueError(f'json={json}, path={path} not supported, json must be a dict')
    if type(path) is not str and type(path) is not list:
        raise ValueError(f'path format {path} not supported, path can be a list of strings like [x,y,z] or a string like x.y.z')

    if type(path) is str:
        path = path.strip('.').split('.')
    key = path[0]
    if key in json.keys():
        return get_json_value_at_path(json[key], path[1:], default)
    else:
        return False, default
