import yaml
from typing import Dict

class UniqueKeyLoader(yaml.SafeLoader):
    """Alters SafeLoader to enable duplicate key detection by the SafeConstructor."""

    def construct_mapping(self, node: yaml.MappingNode, deep: bool = False) -> Dict:
        """Overrides the construct_mapping method of the SafeConstructor to raise a ValueError if duplicate keys
        are found.

        Inspired by and adapated from https://stackoverflow.com/a/63215043
        """
        mapping = []
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key not in mapping:
                mapping.append(key)
            else:
                raise ValueError(key)
        return super().construct_mapping(node, deep)
