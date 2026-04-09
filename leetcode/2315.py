class Solution:
    def countAsterisks(self, s: str) -> int:
        start = False
        end = False
        ast = 0
        for i in range(0,len(s),1):
            if s[i] == "*" and start == False:
                ast += 1
            elif s[i] == "|" and start == False:
                start = True
            elif s[i] == "|" and start == True:
                start = False
        return ast