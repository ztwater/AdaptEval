def batch_generator(items, batch_size):
    itemid=0 # Keeps track of current position in items generator/list
    batch = [] # Empty batch
    for item in items: 
      batch.append(item) # Append items to batch
      if len(batch)==batch_size:
        yield batch
        itemid += batch_size # Increment the position in items
        batch = []
    yield batch # yield last bit
