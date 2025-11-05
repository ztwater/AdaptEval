import yaml
import yamlordereddictloader

datas = yaml.load(open('myfile.yml'), Loader=yamlordereddictloader.Loader)
