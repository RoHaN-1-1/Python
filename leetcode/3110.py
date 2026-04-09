class Solution:
    def scoreOfString(self, s: str) -> int:
        current = 0
        for i in range(0,len(s)-1,1):
            current = current + abs(ord(s[i]) - ord(s[i+1]))
        return current