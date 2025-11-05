import pandas as pd
import numpy as np

In [716]: df = pd.DataFrame({"gene_name": ['SLC45A1', 'NECAP2', 'CLIC4', 'ADC', 'AGBL4'] , "BoolCol": [False, True, False, True, True] },
       index=list("abcde"))

In [717]: df
Out[717]: 
  BoolCol gene_name
a   False   SLC45A1
b    True    NECAP2
c   False     CLIC4
d    True       ADC
e    True     AGBL4

In [718]: np.where(df["BoolCol"] == True)
Out[718]: (array([1, 3, 4]),)

In [719]: select_indices = list(np.where(df["BoolCol"] == True)[0])

In [720]: df.iloc[select_indices]
Out[720]: 
  BoolCol gene_name
b    True    NECAP2
d    True       ADC
e    True     AGBL4
