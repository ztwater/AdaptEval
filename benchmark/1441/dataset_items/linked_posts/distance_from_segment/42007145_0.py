     #distance beetween segment ab and point c in 2D space
getDistance_ort_2 <- function(a, b, c){
  #go to complex numbers
  A<-c(a[1]+1i*a[2],b[1]+1i*b[2])
  q=c[1]+1i*c[2]
  
  #function to get coefficients of line (ab)
  getAlphaBeta <- function(A)
  { a<-Re(A[2])-Re(A[1])
    b<-Im(A[2])-Im(A[1])
    ab<-as.numeric()
    ab[1] <- -Re(A[1])*b/a+Im(A[1])
    ab[2] <-b/a
    if(Im(A[1])==Im(A[2])) ab<- c(Im(A[1]),0)
    if(Re(A[1])==Re(A[2])) ab <- NA
    return(ab)
  }
  
  #function to get coefficients of line ortogonal to line (ab) which goes through point q
  getAlphaBeta_ort<-function(A,q)
  { ab <- getAlphaBeta(A) 
  coef<-c(Re(q)/ab[2]+Im(q),-1/ab[2])
  if(Re(A[1])==Re(A[2])) coef<-c(Im(q),0)
  return(coef)
  }
  
  #function to get coordinates of interception point 
  #between line (ab) and its ortogonal which goes through point q
  getIntersection_ort <- function(A, q){
    A.ab <- getAlphaBeta(A)
    q.ab <- getAlphaBeta_ort(A,q)
    if (!is.na(A.ab[1])&A.ab[2]==0) {
      x<-Re(q)
      y<-Im(A[1])}
    if (is.na(A.ab[1])) {
      x<-Re(A[1])
      y<-Im(q)
    } 
    if (!is.na(A.ab[1])&A.ab[2]!=0) {
      x <- (q.ab[1] - A.ab[1])/(A.ab[2] - q.ab[2])
      y <- q.ab[1] + q.ab[2]*x}
    xy <- x + 1i*y  
    return(xy)
  }
  
  intersect<-getIntersection_ort(A,q)
  if ((Mod(A[1]-intersect)+Mod(A[2]-intersect))>Mod(A[1]-A[2])) {dist<-min(Mod(A[1]-q),Mod(A[2]-q))
  } else dist<-Mod(q-intersect)
  return(dist)
}



 
