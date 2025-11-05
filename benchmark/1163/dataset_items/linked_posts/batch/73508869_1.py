import pandas as pd

my_dictionary = pd.DataFrame({
  'key1': {
    'inner_key1': 'value1'
  },
  'key2': {
    'inner_key2': 'value2'
  }
})

print(my_dictionary.key1.inner_key1)
# Output: value1
