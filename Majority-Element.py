class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        incr = 1
        test = nums[0]

        for num in nums:
            if num == test:
                incr += 1
            else:
                incr -= 1
            
            if incr <= 0:
                test = num
                incr = 1
        
        return test