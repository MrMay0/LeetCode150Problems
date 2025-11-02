class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        n = len(s)
        spaces = 0
        while s[n-1-spaces] == ' ':
            spaces +=1
        while res < n and s[n-1-spaces -res] != ' ':
            res +=1
        return res
        