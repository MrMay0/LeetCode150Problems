class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len (needle)
        if m > n: 
            return -1
        index = 0
        while index <= n-m:
            count = 0
            full_index = index
            while count < m and full_index < n and haystack[full_index] == needle[count]:
                count += 1
                full_index += 1
            if count == m:
                return index
            index += 1
        return - 1