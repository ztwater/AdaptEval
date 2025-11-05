from functools import reduce
from operator import and_

reduce(and_, (x==yourList[0] for x in yourList), True)
