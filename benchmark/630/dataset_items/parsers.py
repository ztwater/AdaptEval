import ast
from typing import Generator
from models import ImportInfo


def get_module_info_from_python_file(path: str) -> Generator[ImportInfo, None, None]:
    """Get imports, based on given filepath.

    Credit:
        https://stackoverflow.com/a/9049549/2448495
    """

    with open(path, encoding="utf-8") as fh:
    # with open(path) as fh:
        root = ast.parse(fh.read(), path)

    for node in ast.iter_child_nodes(root):  # or potentially ast.walk ?
        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):
            module = node.module.split(".") if node.module else []
        else:
            continue

        if hasattr(node, "names"):
            for n in node.names:
                yield ImportInfo(
                    module=module,
                    name=n.name.split("."),
                    alias=n.asname,
                )
