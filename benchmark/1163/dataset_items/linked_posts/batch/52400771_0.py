class myDict(dict):
    def __getattr__(self,val):
        return self[val]


blockBody=myDict()
blockBody['item1']=10000
blockBody['item2']="StackOverflow"
print(blockBody.item1)
print(blockBody.item2)
