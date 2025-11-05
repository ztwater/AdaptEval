template<typename T, typename cmp = std::less<T>>
size_t longestSubsequence(const vector<T> &elements)
{
    if (elements.size() < 2)
        return elements.size();
    vector<T>seq(elements.size(), T());
    seq[0] = elements[0];
    size_t len = 1;
    auto end = next(seq.begin());
    for (size_t i = 1; i < elements.size(); i++) {
        auto pos = std::lower_bound(seq.begin(), end, elements[i], cmp());
        if (pos == end) {
            *end = elements[i];
            end = next(end);
            len++;
        }
        else
            *pos = elements[i];
    }
    return len;
}
