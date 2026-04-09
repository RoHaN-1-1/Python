class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums),1):
            if nums[i] == 0:
                k = nums[i]
                nums.remove(nums[i])
                nums.append(k)