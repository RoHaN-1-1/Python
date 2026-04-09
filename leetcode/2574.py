class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        right = sum(nums)
        left = 0
        answer = []
        for i in range(0,len(nums),1):
            right -= nums[i]
            answer.append(abs(left - right))
            left += nums[i] 
        return answer