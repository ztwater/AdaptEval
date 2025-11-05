import pandas as pd
import numpy as np


def search_coordinate(df_data: pd.DataFrame, search_set: set) -> list:
    nda_values = df_data.values
    tuple_index = np.where(np.isin(nda_values, [e for e in search_set]))
    return [(row, col, nda_values[row][col]) for row, col in zip(tuple_index[0], tuple_index[1])]


if __name__ == '__main__':
    test_datas = [['cat', 'dog', ''],
                  ['goldfish', '', 'kitten'],
                  ['Puppy', 'hamster', 'mouse']
                  ]
    df_data = pd.DataFrame(test_datas)
    print(df_data)
    result_list = search_coordinate(df_data, {'dog', 'Puppy'})
    print(f"\n\n{'row':<4} {'col':<4} {'name':>10}")
    [print(f"{row:<4} {col:<4} {name:>10}") for row, col, name in result_list]
