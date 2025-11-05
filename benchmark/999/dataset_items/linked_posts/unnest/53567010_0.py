import numpy as np
import pandas as pd


def unnest(frame, explode):
    def mesh(values):
        return np.array(np.meshgrid(*values)).T.reshape(-1, len(values))

    data = np.vstack(mesh(row) for row in frame[explode].values)
    return pd.DataFrame(data=data, columns=explode)


df = pd.DataFrame({'A': [1, 2], 'B': [[1, 2], [1, 2]]})
print(unnest(df, ['A', 'B']))  # base
print()

df = pd.DataFrame({'A': [1, 2], 'B': [[1, 2], [3, 4]], 'C': [[1, 2], [3, 4]]})
print(unnest(df, ['A', 'B', 'C']))  # multiple columns
print()

df = pd.DataFrame({'A': [1, 2, 3], 'B': [[1, 2], [1, 2, 3], [1]],
                   'C': [[1, 2, 3], [1, 2], [1, 2]], 'D': ['A', 'B', 'C']})

print(unnest(df, ['A', 'B']))  # uneven length lists
print()
print(unnest(df, ['D', 'B']))  # different types
print()
