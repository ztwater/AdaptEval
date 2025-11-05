def batchify(arr, batch_size):
  num_batches = math.ceil(len(arr) / batch_size)
  return [arr[i*batch_size:(i+1)*batch_size] for i in range(num_batches)]
  
