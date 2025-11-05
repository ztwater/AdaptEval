function ans=distP2S(px,py,vx,vy,wx,wy)
% [px py vx vy wx wy]
  t=( (px-vx)*(wx-vx)+(py-vy)*(wy-vy) )/idist(vx,wx,vy,wy)^2;
  [idist(px,vx,py,vy) idist(px,vx+t*(wx-vx),py,vy+t*(wy-vy)) idist(px,wx,py,wy) ];
  ans(1+(t>0)+(t>1)); % <0 0<=t<=1 t>1     
 end

function d=idist(a,b,c,d)
 d=abs(a-b+1i*(c-d));
end
