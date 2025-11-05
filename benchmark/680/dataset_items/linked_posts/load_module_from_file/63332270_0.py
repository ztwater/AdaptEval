from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
from typing import Optional


def get_module_from_path(path: Path, relative_to: Optional[Path] = None):
    if not relative_to:
        relative_to = Path.cwd()

    abs_path = path.absolute()
    relative_path = abs_path.relative_to(relative_to.absolute())
    if relative_path.name == "__init__.py":
        relative_path = relative_path.parent
    module_name = ".".join(relative_path.with_suffix("").parts)
    mod = module_from_spec(spec_from_file_location(module_name, path))
    return mod


def get_modules_from_folder(folder: Optional[Path] = None, glob_str: str = "*/**/*.py"):
    if not folder:
        folder = Path(".")

    mod_list = []
    for file_path in sorted(folder.glob(glob_str)):
        mod_list.append(get_module_from_path(file_path))

    return mod_list
