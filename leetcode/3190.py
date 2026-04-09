class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(0,len(nums),1):
            remain = nums[i] % 3
            if remain == 1 or remain == 2:
                ops += 1
           # elif remain == 2:
               # ops += 1
        return ops