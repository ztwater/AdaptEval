def import_module_from_file(full_path_to_module):
    """
    Import a module given the full path/filename of the .py file

    Python 3.4

    """

    module = None

    try:

        # Get module name and path from full path
        module_dir, module_file = os.path.split(full_path_to_module)
        module_name, module_ext = os.path.splitext(module_file)

        # Get module "spec" from filename
        spec = importlib.util.spec_from_file_location(module_name,full_path_to_module)

        module = spec.loader.load_module()

    except Exception as ec:
        # Simple error printing
        # Insert "sophisticated" stuff here
        print(ec)

    finally:
        return module
