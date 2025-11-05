from jaraco.windows import filesystem

def has_hidden_attribute(filepath):
    return filesystem.GetFileAttributes(filepath).hidden
