class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(n):
            for k in range(n):
                if k == i:
                    continue
                else:
                    res[i] *= nums[k]

        return res