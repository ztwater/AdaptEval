import numpy as np

trainable_params = np.sum([np.prod(v.get_shape()) for v in model.trainable_weights])
non_trainable_params = np.sum([np.prod(v.get_shape()) for v in model.non_trainable_weights])
total_params = trainable_params + non_trainable_params
    
print(trainable_params)
print(non_trainable_params)
print(total_params)
