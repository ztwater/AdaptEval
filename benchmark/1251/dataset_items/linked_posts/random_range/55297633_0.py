import bisect
import random

def fast_sample(low, high, num):
    """ Samples :param num: integer numbers in range of
        [:param low:, :param high:) without replacement
        by maintaining a list of ranges of values that
        are permitted.

        This list of ranges is used to map a random number
        of a contiguous a range (`r_n`) to a permissible
        number `r` (from `ranges`).
    """
    ranges = [high]
    high_ = high - 1
    while len(ranges) - 1 < num:
        # generate a random number from an ever decreasing
        # contiguous range (which we'll map to the true
        # random number).
        # consider an example with low=0, high=10,
        # part way through this loop with:
        #
        # ranges = [0, 2, 3, 7, 9, 10]
        #
        # r_n :-> r
        #   0 :-> 1
        #   1 :-> 4
        #   2 :-> 5
        #   3 :-> 6
        #   4 :-> 8
        r_n = random.randint(low, high_)
        range_index = bisect.bisect_left(ranges, r_n)
        r = r_n + range_index
        for i in xrange(range_index, len(ranges)):
            if ranges[i] <= r:
                # as many "gaps" we iterate over, as much
                # is the true random value (`r`) shifted.
                r = r_n + i + 1
            elif ranges[i] > r_n:
                break
        # mark `r` as another "gap" of the original
        # [low, high) range.
        ranges.insert(i, r)
        # Fewer values possible.
        high_ -= 1
    # `ranges` happens to contain the result.
    return ranges[:-1]
