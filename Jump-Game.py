class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        else:
            farthest = 0
            for k in range(n):
                if k > farthest:
                    return False
                else:
                    farthest = max(farthest, k + nums[k])
        return True
            