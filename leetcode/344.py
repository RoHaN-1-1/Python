class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        my notes:

        """

        #for i in range(0,len(s)//2+1,1):
            #letter = s[i]
            #s[i] = s[len(s)-1-i]
            #s[len(s)-1-i] = letter
        s = s.reverse()