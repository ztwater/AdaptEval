%Matlab solution by Tim from Cody
function ans=distP2S(x0,y0,x1,y1,x2,y2)
% Point is x0,y0
z=complex(x0-x1,y0-y1);
complex(x2-x1,y2-y1);
abs(z-ans*min(1,max(0,real(z/ans))));
