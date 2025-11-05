import pandas as pd
import numpy as np

df=pd.DataFrame( {'A': ['A1','A2','A3'],
                  'B': ['B1','B2','B3'],
                  'C': [ ['C1.1','C1.2'],['C2.1','C2.2'],'C3'],
                  'columnD': [ 'D1',['D2.1','D2.2', 'D2.3'],['D3.1','D3.2']],
                  })
print('df',df, sep='\n')

def dfListExplode(df, explodeKeys):
    if not isinstance(explodeKeys, list):
        explodeKeys=[explodeKeys]
    # recursive handling of explodeKeys
    if len(explodeKeys)==0:
        return df
    elif len(explodeKeys)==1:
        explodeKey=explodeKeys[0]
    else:
        return dfListExplode( dfListExplode(df, explodeKeys[:1]), explodeKeys[1:])
    # perform explosion/unnesting for key: explodeKey
    dfPrep=df[explodeKey].apply(lambda x: x if isinstance(x,list) else [x]) #casts all elements to a list
    dfIndExpl=pd.DataFrame([[x] + [z] for x, y in zip(dfPrep.index,dfPrep.values) for z in y ], columns=['explodedIndex',explodeKey])
    dfMerged=dfIndExpl.merge(df.drop(explodeKey, axis=1), left_on='explodedIndex', right_index=True)
    dfReind=dfMerged.reindex(columns=list(df))
    return dfReind

dfExpl=dfListExplode(df,['C','columnD'])
print('dfExpl',dfExpl, sep='\n')
