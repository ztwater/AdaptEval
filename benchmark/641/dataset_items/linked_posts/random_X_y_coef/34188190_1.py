def original(prob_matrix, items):
    choices = np.zeros((n,))
    # This is slow, because of the loop in Python
    for i in range(n):
        choices[i] = np.random.choice(items, p=prob_matrix[:,i])
    return choices
