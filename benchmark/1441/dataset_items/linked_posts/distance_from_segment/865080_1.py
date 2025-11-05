real function pdis(a, b, c)
    real, dimension(0:1), intent(in) :: a, b, c
    real, dimension(0:1) :: t, n, ac
    real :: dd
    t = b - a                          ! Vector ab
    dd = sqrt(t(0)**2+t(1)**2)         ! Length of ab
    t = t/dd                           ! unit vector of ab
    n = (/-t(1), t(0)/)                ! normal unit vector to ab
    ac = c - a                         ! vector ac
    pdis = abs(ac(0)*n(0)+ac(1)*n(1))  ! Projection of ac to n (the minimum distance)
end function pdis


program test
    print *, pdis((/1.0,1.0/), (/2.0,2.0/), (/2.0,0.0/))   ! Example (answer is 1.414)
end program test
