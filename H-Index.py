class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        n = len(citations)
        if n == 1:
            return min(1,citations[0])
        else: 
            while h_index < n and h_index < citations[h_index]:
                h_index += 1
            return h_index