def shuffle(self) -> None:
    """
    Shuffles X and Y
    """
    x = self.X.T
    y = self.Y.T
    p = np.random.permutation(len(x))
    self.X = x[p].T
    self.Y = y[p].T
