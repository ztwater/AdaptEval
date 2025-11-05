class Count():
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax

obj1 = Count(1,10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.mycurrent)  --> AttributeError: 'Count' object has no attribute 'mycurrent'
