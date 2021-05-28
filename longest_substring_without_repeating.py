class Solution:
    def lengthOfLongestSubstring(self, s: str):
        n = len(s)
        map_k = {}
        i = 0
        res = 0
        for j in range(n):
            if s[j] in map_k:
                i = max(i, map_k[s[j]])
            res = max(res, j - i + 1)
            map_k[s[j]] = j + 1
        return res