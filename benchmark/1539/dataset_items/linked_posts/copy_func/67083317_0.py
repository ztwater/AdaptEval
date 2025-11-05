def my_copy(f): 
        # Create a lambda that mimics f
        g = lambda *args: f(*args)
        # Add any properties of f
        t = list(filter(lambda prop: not ("__" in prop),dir(f)))
        i = 0
        while i < len(t):
            setattr(g,t[i],getattr(f,t[i]))
            i += 1
        return g
        
# Test
def sqr(x): return x*x
sqr.foo = 500

sqr_copy = my_copy(sqr)
print(sqr_copy(5)) # -> 25
print(sqr_copy(6)) # -> 36
print(sqr_copy.foo) # -> 500
print(sqr_copy == sqr) # -> False
