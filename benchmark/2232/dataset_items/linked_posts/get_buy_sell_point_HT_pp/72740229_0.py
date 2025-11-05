const pivotHigh = (series, period) => {
  
  let ph = 0;
  let phIndex = 0;

  // left + right bars + 1 pivot bar
  for ( let i = period + period + 1, len = series.length; i--; ) {

    const cur = series[len - i];
    
    // [!] > -1 logic. can also checks: NaN
    if ( cur > -1 ) {} else {
      break;
    }

    if ( cur > ph ) {
      ph = cur;
      phIndex = len - i;
    }
  }
  // found?
  return phIndex === period
    ? ph
    : 0;
};
