import numpy as np

def sortoutOutliers(dataIn,factor):
    quant3, quant1 = np.percentile(dataIn, [75 ,25])
    iqr = quant3 - quant1
    iqrSigma = iqr/1.34896
    medData = np.median(dataIn)
    dataOut = [ x for x in dataIn if ( (x > medData - factor* iqrSigma) and (x < medData + factor* iqrSigma) ) ] 
    return(dataOut)
