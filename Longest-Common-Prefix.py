class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        is_prefix = True
        prefix = ''
        count = 0
        n = min(len(s) for s in strs)
        m = len(strs)
        while count < n and is_prefix:
            test = strs[0][count]
            for i in range(m):
                if strs[i][count] != test:
                    is_prefix = False
            if is_prefix:
                prefix += test
            count +=1
        return prefix