class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0
        nbr_jump = 0
        jump_to = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == jump_to:
                jump_to = farthest
                nbr_jump += 1
        return nbr_jump