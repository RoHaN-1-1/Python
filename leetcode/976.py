class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) == 3:
            a = nums[0]
            b = nums[1]
            c= nums[2]
            if a + b > c and a + c > b and b + c > a:
                return a + b + c
        elif len(nums) > 3:
            nums.sort()
            for i in range(len(nums)-1,1,-1):
                if nums[i-1] + nums[i-2] > nums[i]:
                    return nums[i] + nums[i-1] + nums[i-2]
        return 0