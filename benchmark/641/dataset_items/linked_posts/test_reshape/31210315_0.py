    indices = zeros_like(A.indices)
    indices[A.indptr[1:-1]] = A.shape[1]
    indices = cumsum( indices)+A.indices
    A_flat = sparse.csc_matrix((T_rot.data, indices,[0,size(A)]),shape=(prod(A.shape),1))
