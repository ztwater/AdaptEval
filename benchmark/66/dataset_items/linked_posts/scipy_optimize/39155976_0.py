gd = ddot(n,g,1,d,1)
  if (ifun .eq. 0) then
     gdold=gd
     if (gd .ge. zero) then
c                               the directional derivative >=0.
c                               Line search is impossible.
        if (iprint .ge. 0) then
            write(0,*)' ascent direction in projection gd = ', gd
        endif
        info = -4
        return
     endif
  endif
