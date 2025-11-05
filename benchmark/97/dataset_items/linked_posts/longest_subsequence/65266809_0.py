def findLIS(s):
  lengths = [1] * len(s)
  for i in range(1, len(s)):
    for j in range(i):
      if s[i] > s[j] and lengths[i] <= lengths[j]:
        lengths[i] += 1
  return max(lengths)
