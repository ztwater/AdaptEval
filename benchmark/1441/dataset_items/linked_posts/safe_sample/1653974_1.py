@staticmethod
def union(*sets):
    union = OrderedSet()
    union.union(*sets)
    return union

def union(self, *sets):
    for set in sets:
        self |= set
