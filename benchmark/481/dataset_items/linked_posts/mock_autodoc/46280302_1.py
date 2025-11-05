def skip_some_classes(app, what, name, obj, skip, options):
    return skip or name in ('Class',)  # define some better condition here

def setup(app):
    app.connect('autodoc-skip-member', skip_some_classes)
