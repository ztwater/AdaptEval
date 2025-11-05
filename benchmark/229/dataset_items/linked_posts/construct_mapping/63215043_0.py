 import yaml
 # special loader with duplicate key checking
 class UniqueKeyLoader(yaml.SafeLoader):
     def construct_mapping(self, node, deep=False):
         mapping = []
         for key_node, value_node in node.value:
             key = self.construct_object(key_node, deep=deep)
             assert key not in mapping
             mapping.append(key)
         return super().construct_mapping(node, deep)
