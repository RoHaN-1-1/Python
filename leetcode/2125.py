class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cameras = 0
        l = []
        sum = 0
        for i in range(0,len(bank),1):
            cameras = bank[i].count("1")
            if cameras == 0:
                continue
            l.append(cameras)
        for i in range(0,len(l)-1,1):
            sum = sum + l[i] * l[i+1]
        return sum