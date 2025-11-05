def xmltodict(element):
    if not isinstance(element, ElementTree.Element):
        raise ValueError("must pass xml.etree.ElementTree.Element object")

    def xmltodict_handler(parent_element):
        result = dict()
        for element in parent_element:
            if len(element):
                obj = xmltodict_handler(element)
            else:
                obj = element.text

            if result.get(element.tag):
                if hasattr(result[element.tag], "append"):
                    result[element.tag].append(obj)
                else:
                    result[element.tag] = [result[element.tag], obj]
            else:
                result[element.tag] = obj
        return result

    return {element.tag: xmltodict_handler(element)}


def dicttoxml(element):
    if not isinstance(element, dict):
        raise ValueError("must pass dict type")
    if len(element) != 1:
        raise ValueError("dict must have exactly one root key")

    def dicttoxml_handler(result, key, value):
        if isinstance(value, list):
            for e in value:
                dicttoxml_handler(result, key, e)
        elif isinstance(value, basestring):
            elem = ElementTree.Element(key)
            elem.text = value
            result.append(elem)
        elif isinstance(value, int) or isinstance(value, float):
            elem = ElementTree.Element(key)
            elem.text = str(value)
            result.append(elem)
        elif value is None:
            result.append(ElementTree.Element(key))
        else:
            res = ElementTree.Element(key)
            for k, v in value.items():
                dicttoxml_handler(res, k, v)
            result.append(res)

    result = ElementTree.Element(element.keys()[0])
    for key, value in element[element.keys()[0]].items():
        dicttoxml_handler(result, key, value)
    return result

def xmlfiletodict(filename):
    return xmltodict(ElementTree.parse(filename).getroot())

def dicttoxmlfile(element, filename):
    ElementTree.ElementTree(dicttoxml(element)).write(filename)

def xmlstringtodict(xmlstring):
    return xmltodict(ElementTree.fromstring(xmlstring).getroot())

def dicttoxmlstring(element):
    return ElementTree.tostring(dicttoxml(element))
