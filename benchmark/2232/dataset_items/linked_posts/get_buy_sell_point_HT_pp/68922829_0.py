private boolean checkHighOrLow(Candlestick candlestick , int lengthForCheck, int currentCandleIndex, boolean checkForHigh) {
    double currentCandleStickClosePrice = Double.parseDouble(candlestick.getClose());
    for (int i = 0; i < lengthForCheck; i++) {
        double afterCandleStick  = Double.parseDouble(candlestickList.get(currentCandleIndex + i + 1).getClose());
        double beforeCandleStick = Double.parseDouble(candlestickList.get(currentCandleIndex - i - 1).getClose());
        if(checkForHigh) {
            if (afterCandleStick > currentCandleStickClosePrice)
                return false;
            if (beforeCandleStick > currentCandleStickClosePrice)
                return false;
        }else{
            if(afterCandleStick < currentCandleStickClosePrice)
                return false;
            if(beforeCandleStick < currentCandleStickClosePrice)
                return false;
        }
    }
    return true;
}

public void findHighsAndLows(){
    int lengthForCheck = 1;
    int numOfCandles   = candlestickList.size();
    for(int i = lengthForCheck; i < numOfCandles - lengthForCheck; i ++)
    {
         Candlestick currentCandle = candlestickList.get(i);
         if(checkHighOrLow(currentCandle,numOfCandles,lengthForCheck,i,true))
             highs.add(currentCandle);
         if(checkHighOrLow(currentCandle,numOfCandles,lengthForCheck,i,false))
             lows.add(currentCandle);
    }
}
