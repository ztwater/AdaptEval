    indices = zeros_like(A.indices)
    indices[A.indptr[1:-1]] = A.shape[1]
    indices = cumsum( indices)+A.indices

    indices %= N*A.shape[1]
    indptr = r_[0, where(diff(indices)<0)[0]+1, size(A)]
    A_reshaped = sparse.csc_matrix((A.data, indices,indptr),shape=(N*A.shape[1],A.shape[0]/N ))
