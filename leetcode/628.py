class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        temp = 0
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        nums.sort()
        max_m = nums[-1] * nums[-2] * nums[-3]
        if nums[0] and nums[1] < 0:
            temp = nums[0] * nums[1] * nums[-1]
        if temp > max_m:
            return temp
        else:
            return max_m