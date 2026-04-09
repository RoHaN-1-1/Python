class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = 0
        decrease = 0
        n = nums[0]
        for i in range(1,len(nums),1):
            if n > nums[i]:
                decrease = 1
                n = nums[i]
            elif n < nums[i]:
                increase = 1
                n = nums[i]
        if increase == 1 and decrease == 0:
            return True
        if increase == 0 and decrease == 1:
            return True
        if increase == 0 and decrease == 0:
            return True
        if increase == 1 and decrease == 1:
            return False