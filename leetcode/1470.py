class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s = []
        i = 0
        j = n
        for x in range(0,n,1):
            s.append(nums[i])
            s.append(nums[j])
            i += 1
            j += 1
        return s