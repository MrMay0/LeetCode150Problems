class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        count = 0
        n = len(t)
        m = len(s)
        while index < n and count < m:
            if t[index] == s[count]:
                count += 1
            index += 1
        return count == m
        