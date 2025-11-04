class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        n = len(height)
        r = n-1
        maxvol = 0
        while l < r:
            vol = min(height[l],height[r]) * (r-l)
            if maxvol < vol:
                maxvol = vol
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxvol
        