import re
from typing import List 
 
def camel_case_split(identifier: str) -> List[str]:
    """
    Split a camel-cased name into words.

    Args:
        identifier (`str`): The camel-cased name to parse.

    Returns:
        `List[str]`: The list of words in the identifier (as seprated by capital letters).

    Example:

    ```py
    >>> camel_case_split("CamelCasedClass")
    ["Camel", "Cased", "Class"]
    ```
    """
    # Regex thanks to https://stackoverflow.com/questions/29916065/how-to-do-camelcase-split-in-python
    matches = re.finditer(".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", identifier)
    return [m.group(0) for m in matches]

