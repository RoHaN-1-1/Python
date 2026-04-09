class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = []
        for i in range(0,len(nums),1):
            n.append(nums[i]**2)
        n.sort()
        return n
       