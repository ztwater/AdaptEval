from benedict import benedict

dictionary1=benedict({'level1':{'level2':{'levelA':0,'levelB':1}}})
update={'level1':{'level2':{'levelB':10}}}
dictionary1.merge(update)
print(dictionary1)
# >> {'level1':{'level2':{'levelA':0,'levelB':10}}}
