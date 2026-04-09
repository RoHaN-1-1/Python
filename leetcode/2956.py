class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1 = 0
        answer2 = 0
        for i in range(0,len(nums1),1):
            if nums1[i] in nums2:
                answer1 += 1
        for i in range(0,len(nums2),1):
            if nums2[i] in nums1:
                answer2 += 1
        ans = [answer1,answer2]
        return ans 