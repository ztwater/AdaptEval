/* 3x3
X 0 2
X X 1
X X X
*/
static_assert(f(3, 0) == std::pair{0, 1});
static_assert(f(3, 1) == std::pair{1, 2});
static_assert(f(3, 2) == std::pair{0, 2});

// 4x4
static_assert(f(4, 0) == std::pair{0, 1});
static_assert(f(4, 1) == std::pair{1, 2});
static_assert(f(4, 2) == std::pair{2, 3});
static_assert(f(4, 3) == std::pair{0, 2});
static_assert(f(4, 4) == std::pair{1, 3});
static_assert(f(4, 5) == std::pair{0, 3});

/* 5x5
X 0 4 7 9
X X 1 5 8
X X X 2 6
X X X X 3
X X X X X
*/
static_assert(f(5, 0) == std::pair{0, 1});
static_assert(f(5, 1) == std::pair{1, 2});
static_assert(f(5, 2) == std::pair{2, 3});
static_assert(f(5, 3) == std::pair{3, 4});
static_assert(f(5, 4) == std::pair{0, 2});
static_assert(f(5, 5) == std::pair{1, 3});
static_assert(f(5, 6) == std::pair{2, 4});
static_assert(f(5, 7) == std::pair{0, 3});
static_assert(f(5, 8) == std::pair{1, 4});
static_assert(f(5, 9) == std::pair{0, 4});
