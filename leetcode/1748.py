class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = []
        for i in range(0,len(nums),1):
            if nums.count(nums[i]) == 1:
                unique.append(nums[i])
        return sum(unique)