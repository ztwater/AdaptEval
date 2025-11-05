my_pivotlow(float _series = low, int _leftBars, int _rightBars) =>
    float _pivotLow = na
    int _pivotRange = ( _leftBars + _rightBars )
    float _leftEdgeValue = nz(_series[_pivotRange], na)
    if not na(_series) and _leftBars > 0 and _rightBars > 0 and not na(_leftEdgeValue)
        float _possiblePivotLow = _series[_rightBars]
        float[] _arrayOfSeriesValues = array.new_float(0)
        for _barIndex = _pivotRange to 0
            array.push(_arrayOfSeriesValues, _series[_barIndex])
        //end for
        int _pivotLowRightBars = array.size(_arrayOfSeriesValues) - array.lastindexof(_arrayOfSeriesValues, array.min(_arrayOfSeriesValues)) - 1
        _pivotLow := ( _pivotLowRightBars == _rightBars ) ? _possiblePivotLow : na
    //end if
    _pivotLow
