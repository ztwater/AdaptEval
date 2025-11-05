#include <utility>

constexpr std::pair<int, int> f(int n, int idx)
{
    int group_size = n - 1;
    int rest = idx + 1;

    while (rest > group_size)
    {
        rest = rest - group_size;
        --group_size;
    }
    return {(rest - 1) % group_size,
            n - group_size +  (rest - 1) % group_size};
}
