class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = []
        small = 0
        big = 0
        if len(nums1) < len(nums2):
            small = nums1
            big = nums2
        else:
            small = nums2
            big = nums1
        for i in range(0,len(small),1):
            if small[i] in big:
                c.append(small[i])
        return set(c) 