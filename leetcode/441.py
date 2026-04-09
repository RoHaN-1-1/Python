class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        total = 0
        while total <= n:
            i += 1    
            total += i
        if total == n:
            return i
        else:
            return i-1