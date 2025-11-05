from pydash.arrays import chunk
ids = ['22', '89', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '1']
chunk_ids = chunk(ids,5)
print(chunk_ids)
# output: [['22', '89', '2', '3', '4'], ['5', '6', '7', '8', '9'], ['10', '11', '1']]
