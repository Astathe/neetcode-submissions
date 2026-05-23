import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {nums[0]: 1}
        l = []
        for i in range(1, len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1

        top_k_keys = heapq.nlargest(k, m, key=m.get)


        return top_k_keys