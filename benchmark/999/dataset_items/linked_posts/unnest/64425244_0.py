import typing
import pandas as pd

def horizontal_explode(df: pd.DataFrame, col_name: str, new_columns: typing.Union[list, None]=None) -> pd.DataFrame:
    t = pd.DataFrame(df[col_name].tolist(), columns=new_columns, index=df.index)
    return pd.concat([df, t], axis=1)

