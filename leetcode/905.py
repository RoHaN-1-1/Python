class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = []
        b = []
        if len(nums) == 1:
            return nums
        for i in range(0,len(nums),1):
            if nums[i] % 2 == 0:
                n.append(nums[i])
            elif nums[i] % 2 == 1:
                b.append(nums[i])
        n = n + b
        return n