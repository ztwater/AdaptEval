coords <- cbind(x = c(5,6,4,1,1),y = c(0,4,5,5,0))
a <- numeric()
for (i in 1:dim(coords)[1]){
  #print(i)
  q <- i + 1
  if (i == (dim(coords)[1])) q <- 1
  out <- ((coords[q,1]) - (coords[i,1])) * ((coords[q,2]) + (coords[i,2]))
  a[q] <- out
  rm(q,out)
} #end i loop

rm(i)

a <- sum(a) #-ve is anti-clockwise

b <- cbind(x = rev(coords[,1]), y = rev(coords[,2]))

if (a>0) coords <- b #reverses coords if polygon not traced in anti-clockwise direction
