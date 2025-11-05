def generate_oriented_forest(n):
     """Algorithm O from Knuth TAoCP, Fascicle 4, p. 25. """
     p = range(-1,n)
     while True:
         yield p[1:]
         if p[n] > 0:
             p[n] = p[p[n]]
             continue
         for k in range(n-1,0,-1):
             if p[k] != 0: break
         else:
             break
         j = p[k]
         for q in range(1,k):
             if p[k-q] == p[j]: break
         while True:
             p[k] = p[k-q]
             if k==n:
                 break
             k+=1

 if __name__ == "__main__":
     for el in generate_oriented_forest(4):
         print el 
