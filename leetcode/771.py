class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = 0
        for i in range(0,len(jewels),1):
            x += stones.count(jewels[i])
        return x