class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums_behind = 0
        sum1 = []
        for i in range(0,len(nums),1):
                sum1.append(nums[i]+nums_behind)
                nums_behind += nums[i]
        return sum1