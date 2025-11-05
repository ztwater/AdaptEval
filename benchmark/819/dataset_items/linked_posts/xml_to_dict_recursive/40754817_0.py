    def recursive_dict(element):
        return (element.tag.split('}')[1],
                dict(map(recursive_dict, element.getchildren()),
                     **element.attrib))
