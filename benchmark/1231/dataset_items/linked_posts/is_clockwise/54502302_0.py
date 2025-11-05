if (nte[0] >= prv[0] && nxt[0] >= nte[0]) return(CW);
if (nte[0] <= prv[0] && nxt[0] <= nte[0]) return(CCW);
// Okay, it's not easy-peasy, so now, do the math
if (nte[0] * nxt[1] - nte[1] * nxt[0] - prv[0] * (nxt[1] - crt[1]) + prv[1] * (nxt[0] - nte[0]) >= 0) return(CCW); // For quadrant 3 return(CW)
return(CW) // For quadrant 3 return (CCW)
