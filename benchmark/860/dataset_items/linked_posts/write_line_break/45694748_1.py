import sys
import ruamel.yaml

yaml = ruamel.yaml.YAML()
list_of_dicts = yaml.seq([ { 'key_1': 'value_a', 'key_2': 'value_b'},
                           { 'key_1': 'value_c', 'key_2': 'value_d'},
                           { 'key_1': 'value_x', 'key_2': 'value_y'}  ])

for idx in range(1, len(list_of_dicts)):
    list_of_dicts.yaml_set_comment_before_after_key(idx, before='\n')

ruamel.yaml.comments.dump_comments(list_of_dicts)
yaml.dump(list_of_dicts, sys.stdout)
