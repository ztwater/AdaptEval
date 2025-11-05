def randomSample(populationSize, sampleSize):
  populationStr = str(populationSize)
  dTree, samples = {}, []
  for i in range(sampleSize):
    val, dTree = getElem(populationStr, dTree, '')
    samples.append(int(val))
  return samples, dTree
