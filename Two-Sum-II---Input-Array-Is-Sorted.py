class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        n = len(numbers)
        index2 = n-1
        while index1 < index2:
            sum = numbers[index1] + numbers[index2]
            if sum == target:
                return [index1+1, index2+1]
            elif sum < target:
                index1 +=1
            else:
                index2 -=1
        