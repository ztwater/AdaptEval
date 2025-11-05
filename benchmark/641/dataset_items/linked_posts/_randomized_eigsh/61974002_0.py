diag_VtU = np.einsum('ji,ij->j',Vt[:n_components, :], U[:, :n_components])
