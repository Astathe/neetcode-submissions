class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            maxf = 0
            count = {}
            for x in range(i, len(s)):
                count[s[x]] = count.get(s[x], 0) + 1
                maxf = max(maxf, count.get(s[x]))
                if x - i + 1 - maxf <= k:
                    res = max(res, x - i + 1)

        return res