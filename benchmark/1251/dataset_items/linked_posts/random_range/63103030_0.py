def extractSamples(populationSize, sampleSize, intervalLst) :
    import random
    if (sampleSize > populationSize) :
        raise ValueError("sampleSize = "+str(sampleSize) +" > populationSize (= " + str(populationSize) + ")")
    samples = []
    while (len(samples) < sampleSize) :
        i = random.randint(0, (len(intervalLst)-1))
        (a,b) = intervalLst[i]
        sample = random.randint(a,b)
        if (a==b) :
            intervalLst.pop(i)
        elif (a == sample) : # shorten beginning of interval                                                                                                                                           
            intervalLst[i] = (sample+1, b)
        elif ( sample == b) : # shorten interval end                                                                                                                                                   
            intervalLst[i] = (a, sample - 1)
        else :
            intervalLst[i] = (a, sample - 1)
            intervalLst.append((sample+1, b))
        samples.append(sample)
    return samples
