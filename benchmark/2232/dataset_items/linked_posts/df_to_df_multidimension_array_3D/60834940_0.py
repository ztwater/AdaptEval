# function to find an index corresponding
# to current value minus offset value
def prevInd(series, offset, date):
    offset = to_offset(offset)
    end_date = date - offset
    end = series.index.searchsorted(end_date, side="left")
    return end

# function to find an index corresponding
# to the first value greater than current
# it is useful when one has timeseries with non-unique
# but monotonically increasing values
def nextInd(series, date):
    end = series.index.searchsorted(date, side="right")
    return end

def twoColumnsRoll(dFrame, offset, usecols, fn, columnName = 'twoColRol'):
    # find all unique indices
    uniqueIndices = dFrame.index.unique()
    numOfPoints = len(uniqueIndices)
    # prepare an output array
    moving = np.zeros(numOfPoints)
    # nameholders
    price = dFrame[usecols[0]]
    qty   = dFrame[usecols[1]]

    # iterate over unique indices
    for ii in range(numOfPoints):
        # nameholder
        pp = uniqueIndices[ii]
        # right index - value greater than current
        rInd = afta.nextInd(dFrame,pp)
        # left index - the least value that 
        # is bigger or equal than (pp - offset)
        lInd = afta.prevInd(dFrame,offset,pp)
        # call the actual calcuating function over two arrays
        moving[ii] = fn(price[lInd:rInd], qty[lInd:rInd])
    # construct and return DataFrame
    return pd.DataFrame(data=moving,index=uniqueIndices,columns=[columnName])
