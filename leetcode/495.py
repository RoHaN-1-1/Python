class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poi = 0
        t = timeSeries.copy()
        for i in range(0,len(t)-1,1):
            if  t[i+1]  - t[i] > duration:
                poi = poi + duration
            else:
                new = t[i+1] - t[i]
                poi = poi + new
        return poi + duration