filename = 'myimage.png'
imagea = (scipy.misc.imread(filename)).astype(float)

poissonNoise = numpy.random.poisson(imagea).astype(float)

noisyImage = imagea + poissonNoise

#here care must be taken to re cast the result to uint8 if needed or scale to 0-1 etc...
