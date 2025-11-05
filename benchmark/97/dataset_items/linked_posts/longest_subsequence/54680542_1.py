int longestIncreasingSubsequence(const vector<int> &numbers){
    if (numbers.size() < 2)
        return numbers.size();
    vector<int>seq(numbers.size(), numeric_limits<int>::min());
    seq[0] = numbers[0];
    int len = 1;
    vector<int>::iterator end = next(seq.begin());
    for (size_t i = 1; i < numbers.size(); i++) {
        auto pos = std::lower_bound(seq.begin(), end, numbers[i]);
        if (pos == end) {
            *end = numbers[i];
            end = next(end);
            len++;
        }
        else
            *pos = numbers[i];
    }
    return len;
}
