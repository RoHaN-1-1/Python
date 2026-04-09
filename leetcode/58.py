class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " " and flag == 0:
                print("fashdj")
                flag = 1
            if s[i] == " " and flag == 1:
                s = s[i+1:len(s)]
                break
        while s[len(s)-1] == " ":
            s = s[:len(s)-1]
        return len(s)