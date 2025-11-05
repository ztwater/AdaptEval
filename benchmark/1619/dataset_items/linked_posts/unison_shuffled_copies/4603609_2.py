a2 = c[:, :a.size//len(a)].reshape(a.shape)
b2 = c[:, a.size//len(a):].reshape(b.shape)
