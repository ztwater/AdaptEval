import xml.etree.ElementTree as ElementTree

class XmlDictConfig(dict):
    def __init__(self, parent_element):
        if parent_element.items():
            self.updateShim(dict(parent_element.items()))
        for element in parent_element:
            if len(element):
                aDict = XmlDictConfig(element)
                if element.items():
                    aDict.updateShim(dict(element.items()))
                self.updateShim({element.tag: aDict})
            elif element.items():
                self.updateShim({element.tag: dict(element.items())})
            else:
                self.updateShim({element.tag: element.text.strip()})

    def updateShim (self, aDict ):
        for key in aDict.keys():
            if key in self:
                value = self.pop(key)
                if type(value) is not list:
                    listOfDicts = []
                    listOfDicts.append(value)
                    listOfDicts.append(aDict[key])
                    self.update({key: listOfDicts})

                else:
                    value.append(aDict[key])
                    self.update({key: value})
            else:
                self.update(aDict)
