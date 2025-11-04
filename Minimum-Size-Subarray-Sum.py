class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        s = 0
        window = n+1
        while r < n:
            s += nums[r]
            r += 1
            while s >= target:
                window = min(window, r-l)
                s -= nums[l]
                l += 1
        return 0 if window == n+1 else window

        