import copy

temp = copy.deepcopy(elem)
elem.tag = "div"
elem.set("class","wrapper")
elem.clear()
elem.append(temp)
