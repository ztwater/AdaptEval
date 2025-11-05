def murmur3_x86_32(var_0, var_1 = 0):
    var_2 = 0xcc9e2d51
    var_3 = 0x1b873593

    var_4 = len(var_0)
    var_5 = var_1
    var_6 = (var_4 & 0xfffffffc)  # round down to 4 byte block
    for i in range(0, var_6, 4):
      # little endian load order
      var_7 = (ord(var_0[i]) & 0xff) | ((ord(var_0[i + 1]) & 0xff) << 8) | ((ord(var_0[i + 2]) & 0xff) << 16) | (ord(var_0[i + 3]) << 24)
      var_7 *= var_2
      var_7 = (var_7 << 15) | ((var_7 & 0xffffffff) >> 17) # ROTL32(k1,15)
      var_7 *= var_3

      var_5 ^= var_7
      var_5 = (var_5 << 13) | ((var_5 & 0xffffffff) >> 19)  # ROTL32(h1,13)
      var_5 = var_5 * 5 + 0xe6546b64

    # tail
    var_7 = 0

    var_8 = var_4 & 0x03
    if var_8 == 3:
        var_7 = (ord(var_0[var_6 + 2]) & 0xff) << 16
    # fallthrough
    if var_8 in [2, 3]:
        var_7 |= (ord(var_0[var_6 + 1]) & 0xff) << 8
    # fallthrough
    if var_8 in [1, 2, 3]:
        var_7 |= ord(var_0[var_6]) & 0xff
        var_7 *= var_2
        var_7 = (var_7 << 15) | ((var_7 & 0xffffffff) >> 17)  # ROTL32(k1,15)
        var_7 *= var_3
        var_5 ^= var_7

    # finalization
    var_5 ^= var_4

    # fmix(h1)
    var_5 ^= ((var_5 & 0xffffffff) >> 16)
    var_5 *= 0x85ebca6b
    var_5 ^= ((var_5 & 0xffffffff) >> 13)
    var_5 *= 0xc2b2ae35
    var_5 ^= ((var_5 & 0xffffffff) >> 16)

    return var_5 & 0xffffffff
