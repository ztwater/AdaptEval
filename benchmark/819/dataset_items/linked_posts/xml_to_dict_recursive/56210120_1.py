import xml.etree.ElementTree as ET




class XMLToDictionary(dict):
    def __init__(self, parentElement):
        self.parentElement = parentElement
        for child in list(parentElement):
            child.text = child.text if (child.text != None) else  ' '
            if len(child) == 0:
                self.update(self._addToDict(key= child.tag, value = child.text.strip(), dict = self))
            else:
                innerChild = XMLToDictionary(parentElement=child)
                self.update(self._addToDict(key=innerChild.parentElement.tag, value=innerChild, dict=self))

    def getDict(self):
        return {self.parentElement.tag: self}

    class _addToDict(dict):
        def __init__(self, key, value, dict):
            if not key in dict:
                self.update({key: value})
            else:
                identical = dict[key] if type(dict[key]) == list else [dict[key]]
                self.update({key: identical + [value]})


tree = ET.parse('./XML.xml')
root = tree.getroot()
parseredDict = XMLToDictionary(root).getDict()
print(parseredDict)
