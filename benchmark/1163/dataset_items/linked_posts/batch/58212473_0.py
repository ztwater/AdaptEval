from box import Box

mydict = {"key1":{"v1":0.375,
                    "v2":0.625},
          "key2":0.125,
          }
mydict = Box(mydict)

print(mydict.key1.v1)
