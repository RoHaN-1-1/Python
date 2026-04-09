class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        boundary = 0
        step = 0
        for i in range(0,len(nums),1):
            if nums[i] < 0:
                step += nums[i]
            if nums[i] > 0:
                step += nums[i]
            if step == 0:
                boundary += 1
        return boundary