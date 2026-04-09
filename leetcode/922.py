class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e = []
        o = []
        n = []
        for i in range(0,len(nums),1):
            if nums[i] % 2 == 0:
                e.append(nums[i])
            elif nums[i] % 2 == 1:
                o.append(nums[i])
        for i in range(0,len(e),1):
                n.append(e[i])
                n.append(o[i])
        return n