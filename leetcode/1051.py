class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(0,len(expected),1):
            if heights[i] != expected[i]:
                count += 1
        return count