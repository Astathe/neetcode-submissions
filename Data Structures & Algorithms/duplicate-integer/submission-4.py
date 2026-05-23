class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums) - 1): 
            for b in range(i + 1, len(nums)):
                if nums[i] == nums[b]:
                    return True
        return False