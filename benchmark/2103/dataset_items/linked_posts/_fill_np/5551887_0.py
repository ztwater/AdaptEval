# main ideas described in very high level pseudo code
choose suitable base kernel shape and type (gaussian?)
while true
    loop over your array (moving average manner)
        adapt your base kernel to current sparsity pattern
        set current value based on adapted kernel
    break if converged
