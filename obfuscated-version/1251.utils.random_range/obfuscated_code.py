def random_range(var_0, var_1=None, var_2=None):
    import random, math
    # Set a default values the same way "range" does.
    if (var_1 == None): var_0, var_1 = 0, var_0
    if (var_2 == None): var_2 = 1
    # Use a mapping to convert a standard range into the desired range.
    var_3 = lambda i: (i*var_2) + var_0
    # Compute the number of numbers in this range.
    var_4 = (var_1 - var_0) // var_2
    # Seed range with a random integer.
    var_5 = random.randint(0,var_4)
    # 
    # Construct an offset, multiplier, and modulus for a linear
    # congruential generator. These generators are cyclic and
    # non-repeating when they maintain the properties:
    # 
    #   1) "modulus" and "offset" are relatively prime.
    #   2) ["multiplier" - 1] is divisible by all prime factors of "modulus".
    #   3) ["multiplier" - 1] is divisible by 4 if "modulus" is divisible by 4.
    # 
    var_6 = random.randint(0,var_4) * 2 + 1      # Pick a random odd-valued offset.
    var_7 = 4*(var_4//4) + 1                 # Pick a multiplier 1 greater than a multiple of 4.
    var_8 = int(2**math.ceil(math.log2(var_4))) # Pick a modulus just big enough to generate all numbers (power of 2).
    # Track how many random numbers have been returned.
    var_9 = 0
    while var_9 < var_4:
        # If this is a valid value, yield it in generator fashion.
        if var_5 < var_4:
            var_9 += 1
            yield var_3(var_5)
        # Calculate the next value in the sequence.
        var_5 = (var_5*var_7 + var_6) % var_8
