to_drop = pd.DataFrame(to_drop).fillna(True)
to_drop = list(to_drop[to_drop['SalePrice'] <.4 ].index)
df_h1.drop(to_drop,axis=1)
