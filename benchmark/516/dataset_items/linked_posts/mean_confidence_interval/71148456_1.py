-- you should get a mean and a list of nan ci (since data is in wrong format, it thinks its 30 data sets of length 1.
0.1431623130952463 [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan]
-- gives a mean and a list of length 1 for a single CI (since it thinks you have a single dat aset)
0.04947206018132864 [0.40627264]
-- gives 7 CIs for the 7 data sets of length 30. 30 is the number ud want large if you were using z(p)due to the CLT.
-0.03585104402718902 [0.31867309 0.35619134 0.34860011 0.3812853  0.44334033 0.35841138
 0.40739732]
