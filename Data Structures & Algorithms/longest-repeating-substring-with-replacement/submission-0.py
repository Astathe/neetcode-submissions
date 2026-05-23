class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count = {}
            maxf = 0
            for a in range(i, len(s)):
                count[s[a]] = 1 + count.get(s[a], 0)
                maxf= max(maxf, count.get(s[a]))
                if a - i + 1 - maxf <= k:
                    res = max(res, a - i + 1)
        return res
