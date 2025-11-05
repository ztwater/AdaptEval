class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = set()
        for key_node, value_node in node.value:
            each_key = self.construct_object(key_node, deep=deep)
            if each_key in mapping:
                raise ValueError(f"Duplicate Key: {each_key!r} is found in YAML File.\n"
                                 f"Error File location: {key_node.end_mark}")
            mapping.add(each_key)
        return super().construct_mapping(node, deep)

with open(test_suite_full_path, 'r') as f:
    yaml_ret_dict = yaml.load(f, Loader=UniqueKeyLoader)
