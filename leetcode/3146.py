class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        count = 0
        for i in range(0,len(s),1):
            for j in range(0,len(t),1):
                if s[i] == t[j]:
                    count += abs(i-j)
        return count