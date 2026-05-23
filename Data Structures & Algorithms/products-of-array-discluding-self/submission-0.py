class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for k in range(n):
                if i == k:
                    continue
                prod *= nums[k]
            res[i] = prod
        return res