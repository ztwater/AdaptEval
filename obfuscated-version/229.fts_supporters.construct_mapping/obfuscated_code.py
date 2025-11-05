import yaml
# special loader with duplicate key checking
class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, var_0, var_1=False):
        var_2 = []
        for key_node, value_node in var_0.value:
            var_3 = self.construct_object(key_node, var_1=var_1)
            assert var_3 not in var_2
            var_2.append(var_3)
        return super().construct_mapping(var_0, var_1)
