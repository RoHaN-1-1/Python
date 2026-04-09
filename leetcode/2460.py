class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1,1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        for i in range(0,len(nums),1):
            if nums[i] == 0:
                k = nums[i]
                nums.remove(nums[i])
                nums.append(k)
        return nums