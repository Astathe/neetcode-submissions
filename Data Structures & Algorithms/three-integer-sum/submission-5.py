class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        s = []
        seen = set()
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    tupled = tuple((nums[i], nums[l], nums[r]))
                    if tupled not in seen:
                        s.append([nums[i], nums[l], nums[r]])
                        seen.add(tupled)
                    l += 1
                    r -= 1
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1

        return s
