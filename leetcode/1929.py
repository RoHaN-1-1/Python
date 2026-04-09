class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n) # making a list full of zeros with length 2n
        for i in range(0,len(nums),1):
            ans[i] = nums[i] #making the conditions given true
            ans[i+n] = nums[i]
        return ans