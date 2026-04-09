class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        s = []
        for i in range(0,n,1):
            if nums[i] not in s:
                if nums.count(nums[i]) > n/2:
                    return nums[i]
                else:
                    s.append(nums[i])