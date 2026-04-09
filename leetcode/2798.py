class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        meet = 0
        for i in range(0,len(hours),1):
            if hours[i] >= target:
                meet += 1
        return meet