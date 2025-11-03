class Solution:
    def reverseWords(self, s: str) -> str:
        reversed = ''
        n = len(s)
        word = ''
        for i in range(n-1,-1,-1):
            if s[i] != ' ':
                word += s[i]
            elif word:
                reversed += word[::-1].strip()
                reversed += ' '
                word = ''
        if word:
            reversed += word[::-1]
        return reversed.strip()