#get co variance of data
coVar = df.corr() # or df.corr().abs()
threshold = 0.5 # 
"""
1. .where(coVar != 1.0) set NaN where col and index is 1
2. .where(coVar >= threshold) if not greater than threshold set Nan
3. .fillna(0) Fill NaN with 0
4. .sum() convert data frame to serise with sum() and just where is co var greater than threshold sum it
5. > 0 convert all Series to Boolean
"""

coVarCols = coVar.where(coVar != 1.0).where(coVar >=threshold).fillna(0).sum() > 0

# Not Boolean Becuase we need to delete where is co var greater than threshold 
coVarCols = ~coVarCols

# get where you want
df[coVarCols[coVarCols].index]
