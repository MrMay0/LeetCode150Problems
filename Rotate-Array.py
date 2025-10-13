class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        k %= n
        if k == 0:
            return
        inter = nums[-k:]
        for j in range(n - k - 1, -1, -1):
            nums[j + k] = nums[j]
        nums[:k] = inter