xs = [1,2,3,4,5,6,7,8]
from funcy import rpartial
list(map(rpartial(pow, 2), xs))
# [1, 4, 9, 16, 25, 36, 49, 64]
