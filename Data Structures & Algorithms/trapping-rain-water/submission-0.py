class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                if lmax > height[l]:
                    vol += lmax -height[l]
                else:
                    lmax = height[l]
            else:
                r -= 1
                if rmax > height[r]:
                    vol += rmax - height[r]
                else:
                    rmax = height[r]
            
        return vol
            
        