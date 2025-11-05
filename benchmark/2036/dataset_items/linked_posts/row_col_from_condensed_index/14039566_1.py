function PdistIndices(n,indices,m) result(IJ)
    !IJ = {} indices for pdist[python] selected results[indices]
    implicit none
    integer:: i,j,m,n,k,w,indices(0:m-1),IJ(0:m-1,2)
    logical:: finished
    k = 0; w = 0; finished = .false.
    do i=0,n-2
        do j=i+1,n-1
            if (k==indices(w)) then
                IJ(w,:) = [i,j]
                w = w+1
                if (w==m) then
                    finished = .true.
                    exit
                endif
            endif
            k = k+1
        enddo
        if (finished) then
            exit
        endif
    enddo
end function
