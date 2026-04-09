class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ""
        for i in range(0,len(s),1):
            if s[i] == "(":
                if len(stack) != 0:
                    ans = ans + s[i]
                stack.append(s[i])
            if s[i] == ")":
                stack.pop()
                if len(stack) != 0:
                    ans = ans + s[i]
        return ans