unique, idx, counts = torch.unique(A, dim=1, sorted=True, return_inverse=True, return_counts=True)
_, ind_sorted = torch.sort(idx, stable=True)
cum_sum = counts.cumsum(0)
cum_sum = torch.cat((torch.tensor([0]), cum_sum[:-1]))
first_indicies = ind_sorted[cum_sum]
