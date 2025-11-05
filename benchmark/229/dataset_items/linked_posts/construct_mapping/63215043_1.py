 yaml_text = open(filename), 'r').read()
 data[f] = yaml.load(yaml_text, Loader=UniqueKeyLoader)                  
