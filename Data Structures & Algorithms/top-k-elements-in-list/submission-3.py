class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {nums[0]: 1}
        l = []
        for i in range(1, len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
        for a, b in m.items():
            l.append([b, a])

        l.sort()

        res = []

        while len(res) < k:
            res.append(l.pop()[1])
            
        return res