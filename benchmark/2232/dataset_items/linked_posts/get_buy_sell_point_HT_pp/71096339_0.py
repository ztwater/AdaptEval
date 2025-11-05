my_pivothigh(float _series = high, int _leftBars, int _rightBars) =>
    float _pivotHigh = na
    int _pivotRange = ( _leftBars + _rightBars )
    float _leftEdgeValue = nz(_series[_pivotRange], na)
    if not na(_series) and _leftBars > 0 and _rightBars > 0 and not na(_leftEdgeValue)
        float _possiblePivotHigh = _series[_rightBars]
        float[] _arrayOfSeriesValues = array.new_float(0)
        for _barIndex = _pivotRange to 0
            array.push(_arrayOfSeriesValues, _series[_barIndex])
        //end for
        int _pivotHighRightBars = array.size(_arrayOfSeriesValues) - array.lastindexof(_arrayOfSeriesValues, array.max(_arrayOfSeriesValues)) - 1
        _pivotHigh := ( _pivotHighRightBars == _rightBars ) ? _possiblePivotHigh : na
    //end if
    _pivotHigh
