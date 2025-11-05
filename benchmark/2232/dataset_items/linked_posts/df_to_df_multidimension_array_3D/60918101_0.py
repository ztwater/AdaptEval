import pandas as pd

def masscenter(ser: pd.Series, df: pd.DataFrame):
    df_roll = df.loc[ser.index]
    return your_actual_masscenter(df_roll)

masscenter_output = df['price'].rolling(window=3).apply(masscenter, args=(df,))
