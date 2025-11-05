import math

def takespread(sequence, num):
    """
    Get `num` elements from the sequence that are as spread out as possible.

    https://stackoverflow.com/questions/9873626/choose-m-evenly-spaced-elements-from-a-sequence-of-length-n
    :param sequence:
    :param num:
    :return:
    """
    length = float(len(sequence))
    for i in range(num):
        yield sequence[int(math.ceil(i * length / num))]

