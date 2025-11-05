import random

def getElem(populationStr, dTree, key):
  msd  = int(populationStr[0])
  if not key in dTree.keys():
    dTree[key] = range(msd + 1)
  idx = random.randint(0, len(dTree[key]) - 1)
  key = key +  str(dTree[key][idx])
  if len(populationStr) == 1:
    dTree[key[:-1]].pop(idx)
    return key, (percolateUp(dTree, key[:-1]))
  newPopulation = populationStr[1:]
  if int(key[-1]) != msd:
    newPopulation = str(10**(len(newPopulation)) - 1)
  return getElem(newPopulation, dTree, key)

def percolateUp(dTree, key):
  while (dTree[key] == []):
    dTree[key[:-1]].remove( int(key[-1]) )
    key = key[:-1]
  return dTree
