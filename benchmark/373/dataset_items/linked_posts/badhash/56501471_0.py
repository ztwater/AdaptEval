#include <stdint.h>

static inline uint64_t ror64(uint64_t v, int r) {
    return (v >> r) | (v << (64 - r));
}

uint64_t rrxmrrxmsx_0(uint64_t v) {
    v ^= ror64(v, 25) ^ ror64(v, 50);
    v *= 0xA24BAED4963EE407UL;
    v ^= ror64(v, 24) ^ ror64(v, 49);
    v *= 0x9FB21C651E98DF25UL;
    return v ^ v >> 28;
}
