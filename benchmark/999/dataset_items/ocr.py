import pandas as pd

def unnest(df: pd.DataFrame, explode: list, axis: int, suffixes: list = None) -> pd.DataFrame:
    """Unnest specified columns in a DataFrame by exploding values.

    Args:
        df (pd.DataFrame): DataFrame to unnest.
        explode (list): Columns to unnest.
        axis (int): Axis to unnest along (1 for columns, 0 for rows).
        suffixes (list, optional): Suffixes for unnested column names.

    Returns:
        pd.DataFrame: Unnested DataFrame.

    """
    # https://stackoverflow.com/a/53218939
    if axis == 1:
        df1 = pd.concat([df[x].explode() for x in explode], axis=1)
        return df1.join(df.drop(explode, axis=1), how="left")
    else:
        df1 = pd.concat(
            [
                pd.DataFrame(
                    df[x].tolist(),
                    index=df.index,
                    columns=suffixes,
                ).add_prefix(x)
                for x in explode
            ],
            axis=1,
        )
        return df1.join(
            df.drop(explode, axis=1),
            how="left",
        )
