int main()
{
    vector<int> nums = { 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 };
    size_t l = longestSubsequence<int>(nums); // l == 6 , longest increasing subsequence

    nums = { 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 };
    l = longestSubsequence<int, std::greater<int>>(nums); // l == 5, longest decreasing subsequence

    vector<string> vstr = {"b", "a", "d", "bc", "a"};
    l = longestSubsequence<string>(vstr); // l == 2, increasing


    vstr = { "b", "a", "d", "bc", "a" };
    l = longestSubsequence<string, std::greater<string>>(vstr); // l == 3, decreasing

} 
