class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return -1
        for i in range(0,len(nums),1):
            if nums[i] != max(nums) and nums[i] != min(nums):
                return nums[i]
        return -1