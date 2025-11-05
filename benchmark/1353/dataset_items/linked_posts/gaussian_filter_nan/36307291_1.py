array U         1   2   NaN 1   2    
auxiliary V     1   2   0   1   2    
auxiliary W     1   1   0   1   1
position        a   b   c   d   e

filtered VV_b   = 0.25*V_a  + 0.50*V_b  + 0.25*V_c
                = 0.25*1    + 0.50*2    + 0
                = 1.25

filtered WW_b   = 0.25*W_a  + 0.50*W_b  + 0.25*W_c
                = 0.25*1    + 0.50*1    + 0
                = 0.75

ratio Z         = VV_b / WW_b  
                = (0.25*1 + 0.50*2) / (0.25*1    + 0.50*1)
                = 0.333*1 + 0.666*2
                = 1.666
